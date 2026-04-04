from django.db import models
from datetime import date


class BaseWeeklyDelivery(models.Model):
    start_date = models.DateField(default=date.today, help_text="Start date of the week (Monday)")
    end_date = models.DateField(default=date.today, help_text="End date of the week (Friday)")
    video_drive_target = models.IntegerField(default=0)
    video_drive_achieved = models.IntegerField(default=0)
    video_drive_shortfall = models.IntegerField(default=0)
    travel_mobile_target = models.IntegerField(default=0)
    travel_mobile_achieved = models.IntegerField(default=0)
    travel_mobile_shortfall = models.IntegerField(default=0)
    mca_sourcing_target = models.IntegerField(default=0)
    mca_sourcing_achieved = models.IntegerField(default=0)
    mca_sourcing_shortfall = models.IntegerField(default=0)
    total_target = models.IntegerField(default=0)
    total_achieved = models.IntegerField(default=0)
    total_shortfall = models.IntegerField(default=0)
    shortfall_percentage = models.FloatField(default=0.0, help_text="Shortfall percentage, e.g., -80")

    def __str__(self):
        return f"Week: {self.start_date} - {self.end_date}"

    @property
    def week_display(self):
        return f"{self.start_date.strftime('%dth %b')} - {self.end_date.strftime('%dth %b')}"

    class Meta:
        abstract = True


class WeeklyDelivery(BaseWeeklyDelivery):
    class Meta:
        ordering = ['-start_date']  # Most recent first


class WeeklyDeliverySecondary(BaseWeeklyDelivery):
    class Meta:
        ordering = ['-start_date']


class ClientDeliveryStatus(models.Model):
    phase = models.CharField(max_length=100, help_text="Phase (e.g., Phase 1, Phase 2)")
    planned_delivery_date = models.DateField(help_text="Planned Delivery Date")
    planned_delivery_count = models.IntegerField(help_text="Planned Delivery count")
    actual_delivery_date = models.DateField(null=True, blank=True, help_text="Actual Delivery Date")
    actual_delivery_count = models.IntegerField(default=0, help_text="Actual Delivery count")
    no_of_weeks_from_last_delivery = models.IntegerField(null=True, blank=True, help_text="No of weeks from last delivery")
    total_new_poi_delivery_till_date = models.IntegerField(default=0, help_text="Total New POI Delivery till date")
    new_poi_inventory_not_delivered = models.IntegerField(default=0, help_text="New POI Inventory (not delivered to client) as on date")
    comments = models.TextField(blank=True, null=True, help_text="Comments")
    type_of_data = models.CharField(max_length=255, blank=True, null=True, help_text="Type of data (e.g., Drive Coding-51492)")

    def __str__(self):
        return f"{self.phase} - {self.planned_delivery_date.strftime('%d/%b/%y')}"

    class Meta:
        ordering = ['-planned_delivery_date']
        verbose_name = "Client Delivery Status"
        verbose_name_plural = "Client Delivery Statuses"
