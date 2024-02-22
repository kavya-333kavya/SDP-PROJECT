from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('hello2/', hello1),
    path('hello/',hello,name='hello'),
    path('',newhomepage,name='newhomepage'),
    path('travelpackage/',travelpackage,name='travelpackage'),
    path('p/',print1,name='print1'),
    path('h/',print_to_console,name='print_to_console'),
    path('ran1/', ran, name='ran'),
    path('ran/', random123, name='random123'),
    path('date/',get_Date,name='get_Date'),
    path('date1/',getdate1,name="getdate1"),
    path('country/',tzfunctioncall,name="tzfunctioncall"),
    path('z/',modelsfunctioncall,name="modelsfunctioncall"),
    path('x/',registerloginfunction,name="registerloginfunction"),
    path('pie/',pie_chart,name='pie_chart'),
    path('slides/',slidescall,name="slidescall"),
    path('weather/',weatherapgecall,name='weatherapgecall'),
    path('weather1/',weatherlogic,name='weatherlogic'),
    path('login/',login,name='login'),
    path('login1/',login1,name='login1'),
    path('signup/',signup,name='signup'),
    path('signup1/',signup1,name='signup1'),
    path('logout/',logout,name='logout'),
    path('contactmailcall/',contactmailcall,name='contactmailcall'),
    path('contactmail',contactmail,name='contactmail'),
    ]