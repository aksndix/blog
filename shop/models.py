# models.py
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Post(models.Model):
    nameAndFamily = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    numberOfUnit = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.nameAndFamily} - {self.phone} - {self.city} - {self.address} - {self.numberOfUnit}"

class Text(models.Model):
    nameAndFamily = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    text = models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.text} {self.nameAndFamily}"

class Adres(models.Model):
    nameAndFamily = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    numberOfUnit = models.IntegerField(default=1)
    def __str__(self):
        return f"{self.nameAndFamily} - {self.phone} - {self.city} - {self.address} - {self.numberOfUnit}"

class Building(models.Model):
    choices_building_type = [
        ('مسکونی', 'مسکونی'),
        ('اداری', 'اداری'),
        ('سایر', 'سایر'),
    ]
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    typeOfBuilding = models.CharField(max_length=100, choices=choices_building_type)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    initialInventory = models.PositiveIntegerField(default=0)
    date = models.DateField()
    shaba = models.CharField(
        max_length=24,
        default='',
        validators=[RegexValidator(regex='^\\d+$', message='فقط اعداد مجاز هستند')]
    )

    def __str__(self):
        return f"{self.title} {self.typeOfBuilding} {self.city} {self.address} {self.initialInventory} {self.date} {self.shaba}"

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    typeBuilding = models.CharField(max_length=100)
    unit = models.CharField(max_length=10)
    sharedKey = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Bill(models.Model):
    unit = models.ForeignKey(Adres, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    date = models.DateField()
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.unit} - {self.price} - {self.date}"

from django.db import models
from django.contrib.auth.models import User

class MemberRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    typeOfBuilding = models.CharField(max_length=100)
    unit = models.CharField(max_length=10)
    sharedKey = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
