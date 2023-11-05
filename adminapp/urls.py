from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('adminhome',views.adminhome,name='adminhome'),
    path('ahome',views.ahome,name='ahome'),
    path('logout',views.logout,name='logout'),
    path('adminviewdonors',views.adminviewdonors,name='adminviewdonors'),
    path('adminvieworg',views.adminvieworg,name='adminvieworg'),
    path('adminchangepwd',views.adminchangepwd,name='adminchangepwd'),
    path('adminpwdupdated',views.adminpwdupdated,name='adminpwdupdated'),
    path('aupdatedonor/<int:did>',views.aupdatedonor,name='aupdatedonor'),
    path('adonorupdation',views.adonorupdation,name='adonorupdation'),
    path('aupdateorg',views.aupdateorg,name='aupdateorg'),
    path('adeletedonor',views.adeletedonor,name='adeletedonor'),
    path('adeleteorg',views.adeleteorg,name='adeleteorg'),
]

