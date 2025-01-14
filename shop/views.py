from django.shortcuts import render
from .models import Post, Text, Adres, UserInput
from .forms import UserInputForm
from django.contrib import messages

# Create your views here.
def about(request):
    return render(request, 'about-course.html')####################################


def panel(request):
    inputs = UserInput.objects.all()
    return render(request, 'panel.html', {'inputs': inputs})

def assignment(request):
    return render(request, 'assignment.html')

def course(request):
    return render(request, 'course-details.html')####################################

def create_course(request):
    return render(request, 'create-course.html')####################################

def create_quiz(request):
    return render(request, 'create-quiz.html')####################################

def email(request):
    return render(request, 'email.html')

def event(request):
    return render(request, 'event.html')

def forgot_password(request):
    return render(request, 'forgot-password.html')####################################

def index(request):
    return render(request, 'index.html')

def index_2(request):
    return render(request, 'index-2.html')####################################

def index_3(request):
    return render(request, 'index-3.html')####################################

def library(request):
    if request.method == 'POST':
        عنوان = request.POST.get('عنوان')
        نوع_ساختمان = request.POST.get('نوع_ساختمان')
        شهر = request.POST.get('شهر')
        ادرس = request.POST.get('ادرس')
        تعداد_واحد = request.POST.get('تعداد_واحد')
        

        new_address = Adres(
            عنوان=عنوان,
            نوع_ساختمان=نوع_ساختمان,
            شهر=شهر,
            ادرس=ادرس,
            تعداد_واحد=تعداد_واحد,
            
        )
        new_address.save()

        return render(request, 'library.html', {
            'addresses': Adres.objects.all(),
            'success': True
        })

    addresses = Adres.objects.all()
    return render(request, 'library.html', {'addresses': addresses})

def live_class(request):
    return render(request, 'live-class.html')####################################

def mentor_courses(request):
    return render(request, 'mentor-courses.html')####################################

def mentors(request):
    return render(request, 'mentors.html')

def message(request):
    return render(request, 'message.html')
############################################################################################################
def pricing_plan(request):
    if request.method == 'POST': 
        نام_نام_خانوادگی = request.POST['نام_نام_خانوادگی']
        تلفن = request.POST['تلفن'] 
        پیام = request.POST['پیام']

        text = Text(نام_نام_خانوادگی=نام_نام_خانوادگی, تلفن=تلفن, پیام=پیام)
        text.save()

        return render(request, 'pricing_plan.html', {'success': True})

    return render(request, 'pricing_plan.html')
################################################################################################################################################
def publish_course(request):
    return render(request, 'publish-course.html')####################################

def reset_password(request):
    return render(request, 'reset-password.html')####################################

def resources(request):
    return render(request, 'resources.html')

from django.shortcuts import render, redirect


def setting(request):
    if request.method == 'POST': 
        نام_نام_خانوادگی = request.POST['نام_نام_خانوادگی']
        تلفن = request.POST['تلفن'] 
        شهر = request.POST['شهر']
        ادرس = request.POST['ادرس']
        تعداد_واحد = int(request.POST['تعداد_واحد'])  # Convert to integer

        # Rename the instance variable to avoid conflict
        adres_instance = Adres(نام_نام_خانوادگی=نام_نام_خانوادگی, تلفن=تلفن, شهر=شهر, ادرس=ادرس, تعداد_واحد=تعداد_واحد)
        adres_instance.save()

        return render(request, 'setting.html', {'success': True})

    return render(request, 'setting.html')

def sign_in(request):
    return render(request, 'sign-in.html')####################################

def sign_up(request):
    return render(request, 'sign-up.html')####################################

def starred(request):
    return render(request, 'starred.html')

def student_courses(request):
    return render(request, 'student-courses.html')####################################

def students(request):
    return render(request, 'students.html')

def two_step_verification(request):
    return render(request, 'two-step-verification.html')####################################

def upload_videos(request):
    return render(request, 'upload-videos.html')####################################

def veiw_details(request):
    return render(request, 'veiw-details.html')####################################

def verify_email(request):
    return render(request, 'verify-email.html')####################################

def adres1(request):
    addresses = Adres.objects.all()
    return render(request, 'adres1.html', {'addresses': addresses})

def mees(request):
    texts = Text.objects.all()  
    return render(request, 'mees.html', {'texts': texts})


def custom_404_view(request, *args, **kwargs):
    invalid_url = request.path
    return render(request, 'error.html', {
        'invalid_url': invalid_url,
        'error_message': 'آدرس اشتباه است'  
    })

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateBillForm, PayBillForm, UserInputForm, MemberForm, CustomUserCreationForm
from .models import Bill, UserInput, Member

def create_building(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'ساختمان با موفقیت ایجاد شد.')
            return redirect('create_building')
    else:
        form = UserInputForm()
    return render(request, 'create_building.html', {'form': form})

def create_bill(request):
    if request.method == 'POST':
        form = CreateBillForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'قبض با موفقیت ایجاد شد.')
            return redirect('create_bill')
    else:
        form = CreateBillForm()
    return render(request, 'create_bill.html', {'form': form})

def pay_bill(request, bill_id):
    bill = Bill.objects.get(id=bill_id)
    if request.method == 'POST':
        form = PayBillForm(request.POST, instance=bill)
        if form.is_valid():
            form.save()
            messages.success(request, 'پرداخت با موفقیت انجام شد.')
            return redirect('pay_bill', bill_id=bill_id)
    else:
        form = PayBillForm(instance=bill)
    return render(request, 'pay_bill.html', {'form': form, 'bill': bill})
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm, MemberRegistrationForm, UserInputForm

from django.shortcuts import redirect

from django.contrib.auth.models import Group

from django.contrib.auth.models import Group

def register_member(request):
    if not request.session.get('form_filled'):
        messages.error(request, 'لطفا ابتدا فرم را در صفحه آنالیتیکس پر کنید.')
        return redirect('shop:analytics')

    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        member_form = MemberRegistrationForm(request.POST)
        if user_form.is_valid() and member_form.is_valid():
            user = user_form.save()
            member = member_form.save(commit=False)
            member.user = user
            member.save()

            try:
                member_group = Group.objects.get(name='کاربران ساختمان')
                member_group.user_set.add(user)
            except Group.DoesNotExist:
                messages.error(request, "گروه 'کاربران ساختمان' وجود ندارد. لطفا با ادمین سیستم تماس بگیرید.")
                return redirect('shop:register_member')

            messages.success(request, 'عضو با موفقیت ثبت شد.')
            return redirect('shop:register_member')
    else:
        user_form = CustomUserCreationForm()
        member_form = MemberRegistrationForm()

    return render(request, 'register_member.html', {'user_form': user_form, 'member_form': member_form})




from django.contrib.auth.decorators import login_required

@login_required
def analytics(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'داده‌ها با موفقیت ذخیره شدند.')
            request.session['form_filled'] = True
            return redirect('shop:register_member')
    else:
        form = UserInputForm()

    return render(request, 'analytics.html', {'form': form})


from django.contrib.auth.decorators import login_required, user_passes_test

def is_building_manager(user):
    return user.groups.filter(name='مدیر ساختمان').exists() or user.groups.filter(name='کاربران ساختمان').exists()

@login_required
@user_passes_test(is_building_manager)

def shared_page(request):
    # اینجا می‌توانید داده‌ها را ذخیره و پردازش کنید
    return render(request, 'shared_page.html')


from django.contrib.auth.models import Group

def create_groups():
    group_names = ['کاربران ساختمان', 'مدیر ساختمان']
    for group_name in group_names:
        group, created = Group.objects.get_or_create(name=group_name)
        if created:
            print(f"Group '{group_name}' created.")
        else:
            print(f"Group '{group_name}' already exists.")

create_groups()


def login(request):
    return render(request, 'login.html')