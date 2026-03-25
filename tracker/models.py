from django.db import models
from datetime import date

class WeeklyDelivery(models.Model):
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
        ordering = ['-start_date']  # Most recent first
