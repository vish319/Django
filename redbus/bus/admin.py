from django.contrib import admin
from .models import bus_details

# Register your models here.
class busdetailsadmin(admin.ModelAdmin):
      list_display = ['bname','bdate','bprice','bfrom','bto']

admin.site.register(bus_details,busdetailsadmin)
