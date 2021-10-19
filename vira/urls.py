from django.urls import path
from vira.Views import MainView

app_name = 'vira'
urlpatterns = [
    # Dashboard
    path('main/', MainView.view_main, name='view_main'),
]
