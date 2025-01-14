# models.py
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Post(models.Model):
    نام_نام_خانوادگی = models.CharField(max_length=30)
    تلفن = models.CharField(max_length=15)
    شهر = models.CharField(max_length=20)
    ادرس = models.CharField(max_length=255)
    تعداد_واحد = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.نام_نام_خانوادگی} - {self.تلفن} - {self.شهر} - {self.ادرس} - {self.تعداد_واحد}"

class Text(models.Model):
    نام_نام_خانوادگی = models.CharField(max_length=30)
    تلفن = models.CharField(max_length=11)
    پیام = models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.پیام} {self.نام_نام_خانوادگی}"

class Adres(models.Model):
    نام_نام_خانوادگی = models.CharField(max_length=30)
    تلفن = models.CharField(max_length=15)
    شهر = models.CharField(max_length=20)
    ادرس = models.CharField(max_length=255)
    تعداد_واحد = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.نام_نام_خانوادگی} - {self.تلفن} - {self.شهر} - {self.ادرس} - {self.تعداد_واحد}"

class UserInput(models.Model):
    نوع_ساختمان_choices = [
        ('مسکونی', 'مسکونی'),
        ('اداری', 'اداری'),
        ('سایر', 'سایر'),
    ]
    عنوان = models.CharField(max_length=100)
    نوع_ساختمان = models.CharField(max_length=100, choices=نوع_ساختمان_choices)
    شهر = models.CharField(max_length=100)
    آدرس = models.CharField(max_length=255)
    موجودی_اولیه = models.PositiveIntegerField(default=0)
    تاریخ = models.DateField()
    شبا = models.CharField(
        max_length=24,
        default='',
        validators=[RegexValidator(regex='^\\d+$', message='فقط اعداد مجاز هستند')]
    )

    def __str__(self):
        return f"{self.عنوان} {self.نوع_ساختمان} {self.شهر} {self.آدرس} {self.موجودی_اولیه} {self.تاریخ} {self.شبا}"

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    نوع_ساختمان = models.CharField(max_length=100)
    واحد = models.CharField(max_length=10)
    رمز_مشترک = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Bill(models.Model):
    واحد = models.ForeignKey(Adres, on_delete=models.CASCADE)
    مبلغ = models.PositiveIntegerField()
    تاریخ = models.DateField()
    پرداخت_شده = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.واحد} - {self.مبلغ} - {self.تاریخ}"

from django.db import models
from django.contrib.auth.models import User

class MemberRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    نوع_ساختمان = models.CharField(max_length=100)
    واحد = models.CharField(max_length=10)
    رمز_مشترک = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
