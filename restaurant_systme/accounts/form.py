from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    
class SignupForm(forms.Form):
    ROLE_CHOICES = [
        ('Cashier', 'Cashier'),
        ('Admin', 'Admin'),
    ]

    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=True)
    terms = forms.BooleanField(required=True, label="I agree to the Terms and Conditions")
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        role = cleaned_data.get("role")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        if role == 'Admin':
            cleaned_data['is_staff'] = True
            cleaned_data['is_superuser'] = True
        else:
            cleaned_data['is_staff'] = False
            cleaned_data['is_superuser'] = False

        return cleaned_data
