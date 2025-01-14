from django.contrib import admin
from .models import Post, Text, Adres, UserInput, Bill

class TextAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'نام_نام_خانوادگی', 'تلفن', 'پیام'] 
    list_filter = ['نام_نام_خانوادگی', 'تلفن', 'پیام']  
    ordering = ['نام_نام_خانوادگی'] 

class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'نام_نام_خانوادگی', 'تلفن', 'شهر', 'ادرس', 'تعداد_واحد']
    list_filter = ['تلفن', 'شهر']  
    ordering = ['نام_نام_خانوادگی', 'شهر']  
    search_fields = ['نام_نام_خانوادگی', 'تلفن', 'شهر'] 

class AdresAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'نام_نام_خانوادگی', 'تلفن', 'شهر', 'ادرس', 'تعداد_واحد']
    list_filter = ['تلفن', 'شهر']  
    ordering = ['نام_نام_خانوادگی', 'شهر', 'تعداد_واحد']  
    search_fields = ['نام_نام_خانوادگی', 'تلفن', 'شهر'] 

class UserInputAdmin(admin.ModelAdmin):
    list_display = ['عنوان', 'نوع_ساختمان', 'شهر', 'آدرس', 'موجودی_اولیه', 'تاریخ', 'شبا']
    list_filter = ['نوع_ساختمان', 'موجودی_اولیه']  
    ordering = ['عنوان', 'شهر']  
    search_fields = ['عنوان', 'نوع_ساختمان', 'شهر']

class BillAdmin(admin.ModelAdmin):
    list_display = ['واحد', 'مبلغ', 'تاریخ', 'پرداخت_شده']
    list_filter = ['واحد', 'پرداخت_شده', 'تاریخ']
    ordering = ['تاریخ', 'واحد']
    search_fields = ['واحد__نام_نام_خانوادگی', 'واحد__تلفن', 'تاریخ']

from django.contrib import admin
from .models import MemberRegistration

class MemberRegistrationAdmin(admin.ModelAdmin):
    list_display = ['get_email', 'get_password', 'نوع_ساختمان', 'واحد', 'رمز_مشترک']
    search_fields = ['user__username', 'نوع_ساختمان', 'واحد']

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
admin.site.register(UserInput, UserInputAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Bill, BillAdmin)

#class AdresAdmin(admin.ModelAdmin):
    #list_display = ['__str__', 'تعداد_واحد', 'تاریخ_ثبت']
    #list_filter = ['شهر']  
   # ordering = ['نام_نام_خانوادگی', 'شهر', 'تعداد_واحد']  
    #search_fields = ['نام_نام_خانوادگی', 'تلفن', 'شهر'] 