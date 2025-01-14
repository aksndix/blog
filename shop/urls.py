from django.urls import path, re_path
from .views import *
from . import views
from .views import custom_404_view

app_name = 'shop'

urlpatterns = [
    path('shared_page/', shared_page, name='shared_page'),
    path('create_building/', create_building, name='create_building'),
    path('create_bill/', create_bill, name='create_bill'),
    path('pay_bill/<int:bill_id>/', pay_bill, name='pay_bill'),
    path('register_member/', views.register_member, name='register_member'),
    path('analytics/', analytics, name='analytics'),
    path('about/', about, name='about'),
    path('assignment/', assignment, name='assignment'),
    path('course/', course, name='course'),
    path('create_course/', create_course, name='create_course'),
    path('create-quiz/', create_quiz, name='create_quiz'),
    path('email/', email, name='email'),
    path('event/', event, name='event'),
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('index/', index, name='index'),
    path('index-2/', index_2, name='index-2'),
    path('index-3/', index_3, name='index-3'),
    path('library/', library, name='library'),
    path('live-class/', live_class, name='live-class'),
    path('mentor_courses/', mentor_courses, name='mentor_courses'),
    path('mentors/', mentors, name='mentors'),
    path('message/', message, name='message'),
    path('pricing_plan/', pricing_plan, name='pricing_plan'),
    path('publish_course/', publish_course, name='publish_course'),
    path('reset-password/', reset_password, name='reset_password'),
    path('resources/', resources, name='resources'),
    path('setting/', setting, name='setting'),
    path('sign_in/', sign_in, name='sign_in'),
    path('sign_up/', sign_up, name='sign_up'),
    path('starred/', starred, name='starred'),
    path('student_courses/', student_courses, name='student_courses'),
    path('students/', students, name='students'),
    path('two_step_verification/', two_step_verification, name='two_step_verification'),
    path('upload-videos/', upload_videos, name='upload_videos'),
    path('veiw-details/', veiw_details, name='veiw_details'),
    path('verify-email/', verify_email, name='verify_email'),
    path('adres1/', adres1, name='adres1'),
    path('mees/', mees, name='mees'),
    path('panel/', panel, name='panel'),
    re_path(r'^.*$', custom_404_view, name='custom_404'),
]
