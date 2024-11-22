from django import forms    
from django.contrib.auth.models import User
from .models import Profile

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
        fields = ['username', 'first_name', 'last_name', 'role']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:  # If editing existing user
            self.fields['role'].initial = 'Admin' if self.instance.is_superuser and self.instance.is_staff else 'Cashier'

    def save(self, commit=True):
        user = super().save(commit=False)
        # Set user permissions based on role
        if self.cleaned_data['role'] == 'Admin':
            user.is_superuser = True
            user.is_staff = True
        else:
            user.is_superuser = False
            user.is_staff = False
        
        if commit:
            user.save()
        return user

class UserCreateForm(UserForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    
    class Meta(UserForm.Meta):
        fields = UserForm.Meta.fields + ['password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        # Set user permissions based on role
        if self.cleaned_data['role'] == 'Admin':
            user.is_superuser = True
            user.is_staff = True
        else:
            user.is_superuser = False
            user.is_staff = False
            
        if commit:
            user.save()
        return user