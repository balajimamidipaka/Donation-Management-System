from django.contrib import admin

from .models import Admin, Organisation,Donor,Donororgmapping

admin.site.register(Admin)
admin.site.register(Organisation)
admin.site.register(Donor)
admin.site.register(Donororgmapping)
