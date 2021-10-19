# import patterns as patterns
from django.urls import path

from accounts import views

app_name = "accounts"

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.login, name='login'),
    path(r'forgot/', views.forgot, name='forgot'),
    path(r'logout/', views.pagelogout, name='logout'),
    path(r'newpassword', views.updateUrlProfile, name='newPassword'),
]
