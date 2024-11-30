from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    ROLE_CHOICES = [
        ('Cashier', 'Cashier'),
        ('Admin', 'Admin'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Cashier')

    def __str__(self):
        return f"{self.user.username}'s profile"

class UserForm(forms.ModelForm):
    ROLE_CHOICES = [
        ('Cashier', 'Cashier'),
        ('Admin', 'Admin'),
    ]
    
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:  # If editing existing user
            # Try to get the role from the associated profile
            try:
                self.fields['role'].initial = self.instance.profile.role
            except Profile.DoesNotExist:
                self.fields['role'].initial = 'Cashier'

    def save(self, commit=True):
        user = super().save(commit=False)
        
        # Save user first
        if commit:
            user.save()
        
        # Create or update associated profile
        profile, created = Profile.objects.get_or_create(
            user=user, 
            defaults={'role': self.cleaned_data['role']}
        )
        
        # Update role if not created
        if not created:
            profile.role = self.cleaned_data['role']
            profile.save()
        
        # Set user permissions based on role
        user.is_superuser = self.cleaned_data['role'] == 'Admin'
        user.is_staff = self.cleaned_data['role'] == 'Admin'
        user.save()
        
        return user

class UserCreateForm(UserForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    
    class Meta(UserForm.Meta):
        fields = UserForm.Meta.fields + ['password']

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        
        # Set password
        user.set_password(self.cleaned_data['password'])
        
        # Save user
        if commit:
            user.save()
        
        # Create profile
        profile, created = Profile.objects.get_or_create(
            user=user, 
            defaults={'role': self.cleaned_data['role']}
        )
        
        # Set user permissions based on role
        user.is_superuser = self.cleaned_data['role'] == 'Admin'
        user.is_staff = self.cleaned_data['role'] == 'Admin'
        user.save()
        
        return user

# Signal receivers can be simplified or removed as we're now handling profile creation in the form
@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)