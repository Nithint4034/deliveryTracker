from django.contrib import admin

from .models import WeeklyDelivery, WeeklyDeliverySecondary, ClientDeliveryStatus


admin.site.register(WeeklyDelivery)
admin.site.register(WeeklyDeliverySecondary)
admin.site.register(ClientDeliveryStatus)
