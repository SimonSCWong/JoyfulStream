# hotels/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password1', widget=forms.PasswordInput)

class CustomUserCreationForm(UserCreationForm):
    confirmed_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)



    def clean_email(self):
        email = self.cleaned_data.get("email")
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use. Please choose a different one.")
        return email
    

    def clean_confirmed_password(self):
        password1 = self.cleaned_data.get("password1")
        confirmed_password = self.cleaned_data.get("confirmed_password")
        if password1 and confirmed_password and password1 != confirmed_password:
            raise forms.ValidationError("Passwords do not match.")
        return confirmed_password
    
# class CustomUserChangeForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ('email', 'is_staff', 'is_active')
#     widgets = {
#         'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
#         'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
#     }
#     labels = {
#         'is_staff': 'Staff Status',
#         'is_active': 'Active Status',
#     }
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if CustomUser.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError("This email is already in use. Please choose a different one.")
        return email

class CustomUserLoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)
    password1 = forms.CharField(label='Password1', widget=forms.PasswordInput, max_length=50)

    def email(self):
        email = self.cleaned_data.get("email")
        if not CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is not registered.")
        return email
    
    
    # def is_staff(self):
    #     is_staff = self.cleaned_data.get("is_staff")
    #     if not CustomUser.objects.filter(is_staff=is_staff).exists():
    #         raise forms.ValidationError("This user is not a staff member.")
    #     return is_staff
    # def is_active(self):
    #     is_active = self.cleaned_data.get("is_active")
    #     if not CustomUser.objects.filter(is_active=is_active).exists():
    #         raise forms.ValidationError("This user is not active.")
    #     return is_active
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password1 = cleaned_data.get("password1")

    # if email and password1:
    #     try:
    #         user = CustomUser.objects.get(email=email)
    #         if not user.check_password(password1):
    #             raise forms.ValidationError("Incorrect password.")
    #     except CustomUser.DoesNotExist:
    #             raise forms.ValidationError("This email is not registered.")
    #     if not user.is_active:
    #         raise forms.ValidationError("This account is inactive.")
    #     if not user.is_staff:
    #         raise forms.ValidationError("This account is not a staff member.")
    #     else:
    #         raise forms.ValidationError("Email and password are required.")
    
    
    
    
    # def password1(self): 
    #     password1 = self.cleaned_data.get("password1")
    #     CustomUser.objects.filter(password1=password1).exists()
    #     except MyExceptionClass as e:
    #     finally:   
    #         raise forms.ValidationError("This email is not registered.")
    # return password1 
        
    # def confirmed_password(self):
    #     confirmed_password = self.cleaned_data.get("confirmed_password")
    #     if not CustomUser.objects.filter(confirmed_password=confirmed_password).exists():
    #         raise forms.ValidationError("This confirmed password is not active.")
    #     return confirmed_password
