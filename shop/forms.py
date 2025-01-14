# forms.py
from django import forms
from .models import Bill, UserInput, Member
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateBillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['واحد', 'مبلغ', 'تاریخ']

class PayBillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['پرداخت_شده']

class UserInputForm(forms.ModelForm):
    class Meta:
        model = UserInput
        fields = ['عنوان', 'نوع_ساختمان', 'شهر', 'آدرس', 'موجودی_اولیه', 'تاریخ', 'شبا']

    نوع_ساختمان = forms.ChoiceField(choices=UserInput.نوع_ساختمان_choices)

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['نوع_ساختمان', 'واحد', 'رمز_مشترک']

    نوع_ساختمان = forms.CharField()

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
        fields = ['نوع_ساختمان', 'واحد', 'رمز_مشترک']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
