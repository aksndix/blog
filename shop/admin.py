from django.contrib import admin
from .models import Post, Text, Adres, Building, Bill

class TextAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'nameAndFamily', 'phone', 'text']
    list_filter = ['nameAndFamily', 'phone', 'text']
    ordering = ['nameAndFamily']

class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'nameAndFamily', 'phone', 'city', 'address', 'numberOfUnit']
    list_filter = ['phone', 'city']
    ordering = ['nameAndFamily', 'city']
    search_fields = ['nameAndFamily', 'phone', 'city']

class AdresAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'nameAndFamily', 'phone', 'city', 'address', 'numberOfUnit']
    list_filter = ['phone', 'city']
    ordering = ['nameAndFamily', 'city', 'numberOfUnit']
    search_fields = ['nameAndFamily', 'phone', 'city']

class UserInputAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'typeOfBuilding', 'city', 'address', 'initialInventory', 'date', 'shaba']
    list_filter = ['typeOfBuilding', 'initialInventory']
    ordering = ['title', 'city']
    search_fields = ['title', 'typeOfBuilding', 'city']

class BillAdmin(admin.ModelAdmin):
    list_display = ['unit', 'price', 'date', 'paid']
    list_filter = ['unit', 'paid', 'date']
    ordering = ['date', 'unit']
    search_fields = ['واحد__نام_نام_خانوادگی', 'واحد__تلفن', 'date']

from django.contrib import admin
from .models import MemberRegistration

class MemberRegistrationAdmin(admin.ModelAdmin):
    list_display = ['get_email', 'get_password', 'typeOfBuilding', 'unit', 'sharedKey']
    search_fields = ['user__username', 'typeOfBuilding', 'unit']

    def get_email(self, obj):
        return obj.user.email
    get_email.admin_order_field = 'user__email'
    get_email.short_description = 'Email'

    def get_password(self, obj):
        return obj.user.password
    get_password.admin_order_field = 'user__password'
    get_password.short_description = 'Password'

admin.site.register(MemberRegistration, MemberRegistrationAdmin)
admin.site.register(Text, TextAdmin)  
admin.site.register(Adres, AdresAdmin) 
admin.site.register(Building, UserInputAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Bill, BillAdmin)

#class AdresAdmin(admin.ModelAdmin):
    #list_display = ['__str__', 'تعداد_واحد', 'تاریخ_ثبت']
    #list_filter = ['شهر']  
   # ordering = ['نام_نام_خانوادگی', 'شهر', 'تعداد_واحد']  
    #search_fields = ['نام_نام_خانوادگی', 'تلفن', 'شهر'] 