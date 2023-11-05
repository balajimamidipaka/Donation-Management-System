from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
       path('donorhome',views.donorhome,name='donorhome'),
       path('donordonate',views.donordonate,name='donordonate'),
       path('donorchangepwd',views.donorchangepwd,name="donorchangepwd"),
       path('donorpwdupdated',views.donorpwdupdated,name="donorpwdupdated"),
       path('donormakedonation',views.donormakedonation,name='donormakedonation'),
       path('donordonated',views.donordonated,name='donordonated'),
       path('donormydonations',views.donormydonations,name='donormydonations'),

]