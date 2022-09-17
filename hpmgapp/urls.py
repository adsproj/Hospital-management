from unicodedata import name
from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.firstpage,name='firstpage'),
    path('appointment',views.appointment,name='appointment'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('signuppage',views.signuppage,name='signuppage'),
    path('appointment_success',views.appointment_success,name='appointment_success'),
    path('patient_details',views.patient_details,name='patient_details'),

    path('usercreate/',views.usercreate,name="usercreate"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout")
]