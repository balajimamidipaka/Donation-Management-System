from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
      path('orghome',views.organisationhome,name='organisationhome'),
      path("orgchangepwd",views.orgchangepwd,name="orgchangepwd"),
      path("orgpwdupdated",views.orgpwdupdated,name="orgpwdupdated"),
      path('orgdonors', views.orgdonors, name='orgdonors'),
]