# forms.py
from django import forms
from .models import Bill, Building, Member
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateBillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['unit', 'price', 'date']

class PayBillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['paid']

class UserInputForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ['title', 'typeOfBuilding', 'city', 'address', 'initialInventory', 'date', 'shaba']

    typeOfBuilding = forms.ChoiceField(choices=Building.choices_building_type)

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['typeOfBuilding', 'unit', 'sharedKey']

    typeOfBuilding = forms.CharField()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

from django import forms
from .models import MemberRegistration
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MemberRegistrationForm(forms.ModelForm):
    class Meta:
        model = MemberRegistration
        fields = ['typeOfBuilding', 'unit', 'sharedKey']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
