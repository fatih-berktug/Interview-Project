from django.urls import path
from vira.Views import MainView,DoctorViews

app_name = 'vira'
urlpatterns = [
    # Dashboard
    path('main/', MainView.view_main, name='view_main'),
    #Doctor
    path('doctor/', DoctorViews.view_doctor, name='view_doctor'),
]
