from .models import User,Turffdetails,Tbooking,owner
from django import forms


class UserForm(forms.ModelForm):
    """Form definition for User."""
    password= forms.CharField(
        widget=forms.PasswordInput()
    )
    confirm_password= forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput()
    )
    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = ('first_name','last_name','username','email','phone','password')

class OwnerForm(forms.ModelForm):
    """Form definition for Owner."""

    class Meta:
        """Meta definition for Ownerform."""

        model = owner
        fields = ('reg_no',)



class TurffdetailsForm(forms.ModelForm):
    """Form definition for Turffdetails."""

    class Meta:
        """Meta definition for Turffdetailsform."""

        model = Turffdetails
        exclude=('turff_owner',)

class TbookingForm(forms.ModelForm):
    """Form definition for Tbooking."""

    class Meta:
        """Meta definition for Tbookingform."""

        model = Tbooking
        exclude=('c_name','detail',)

