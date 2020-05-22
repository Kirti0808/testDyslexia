from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('test1', views.test1, name='test1'),
    path('logout', views.logout, name='logout'),
]
