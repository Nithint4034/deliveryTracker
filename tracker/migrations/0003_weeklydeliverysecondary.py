import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_alter_weeklydelivery_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklyDeliverySecondary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=datetime.date.today, help_text='Start date of the week (Monday)')),
                ('end_date', models.DateField(default=datetime.date.today, help_text='End date of the week (Friday)')),
                ('video_drive_target', models.IntegerField(default=0)),
                ('video_drive_achieved', models.IntegerField(default=0)),
                ('video_drive_shortfall', models.IntegerField(default=0)),
                ('travel_mobile_target', models.IntegerField(default=0)),
                ('travel_mobile_achieved', models.IntegerField(default=0)),
                ('travel_mobile_shortfall', models.IntegerField(default=0)),
                ('mca_sourcing_target', models.IntegerField(default=0)),
                ('mca_sourcing_achieved', models.IntegerField(default=0)),
                ('mca_sourcing_shortfall', models.IntegerField(default=0)),
                ('total_target', models.IntegerField(default=0)),
                ('total_achieved', models.IntegerField(default=0)),
                ('total_shortfall', models.IntegerField(default=0)),
                ('shortfall_percentage', models.FloatField(default=0.0, help_text='Shortfall percentage, e.g., -80')),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
    ]
