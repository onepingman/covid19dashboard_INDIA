from django.contrib import admin
from .models import DailyStateData,DailyTotalcases
# Register your models here.
admin.site.register(DailyStateData)
admin.site.register(DailyTotalcases)