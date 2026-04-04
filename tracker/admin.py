from django.contrib import admin

from .models import WeeklyDelivery, WeeklyDeliverySecondary


admin.site.register(WeeklyDelivery)
admin.site.register(WeeklyDeliverySecondary)
