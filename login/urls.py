from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('test1', views.test1, name='test1'),
    path('test2', views.test2, name='test2'),
    path('test2/start', views.test2Start, name='test2-start'),
    path('test2/stop', views.test2Stop, name='test2-stop'),
    path('test3', views.test3, name='test3'),
    path('logout', views.logout, name='logout'),
]
