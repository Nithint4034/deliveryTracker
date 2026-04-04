from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import WeeklyDelivery


class DeliveryCreateViewTests(TestCase):
	def setUp(self):
		user_model = get_user_model()
		self.user = user_model.objects.create_user(username='tester', password='Password123!')
		self.client.login(username='tester', password='Password123!')

	def test_create_form_prefills_target_fields_from_latest_entry(self):
		WeeklyDelivery.objects.create(
			start_date=date(2026, 3, 2),
			end_date=date(2026, 3, 6),
			video_drive_target=11,
			travel_mobile_target=22,
			mca_sourcing_target=33,
		)
		WeeklyDelivery.objects.create(
			start_date=date(2026, 3, 9),
			end_date=date(2026, 3, 13),
			video_drive_target=44,
			travel_mobile_target=55,
			mca_sourcing_target=66,
		)

		response = self.client.get(reverse('delivery_create'))

		form = response.context['form']
		self.assertEqual(form['video_drive_target'].value(), 44)
		self.assertEqual(form['travel_mobile_target'].value(), 55)
		self.assertEqual(form['mca_sourcing_target'].value(), 66)

	def test_create_form_uses_model_defaults_when_no_previous_entry_exists(self):
		response = self.client.get(reverse('delivery_create'))

		form = response.context['form']
		self.assertEqual(form['video_drive_target'].value(), 0)
		self.assertEqual(form['travel_mobile_target'].value(), 0)
		self.assertEqual(form['mca_sourcing_target'].value(), 0)
