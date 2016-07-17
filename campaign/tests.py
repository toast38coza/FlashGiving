from django.test import TestCase, Client

from .models import *

class HomePageTestCase(TestCase):

	def setUp(self):
		self.c = Client()

	def test_get_is_200(self):

		response = self.c.get("/")
		assert response.status_code == 200

class CampaignPageTestCase(TestCase):

	def setUp(self):
		self.c = Client()

	def test_get_is_200(self):

		response = self.c.get("/nonexistant-campaign/")
		assert response.status_code == 404, \
			'Expect 404. Got: {}' . format (response.status_code)

class CharityModelTestCase(TestCase):

	def setUp(self):
		self.charity = Charity.quick_create()

	def test_get_gateway_properties(self):

		GatewayProperty.objects.create(charity=self.charity, key='foo', value='bar')
		GatewayProperty.objects.create(charity=self.charity, key='baz', value='bus')

		props = self.charity.gateway_properties
		assert props.get('foo') == 'bar'
		assert props.get('baz') == 'bus'

class ModelsTestCase(TestCase):

	def test_charity_quick_create(self):
		Charity.quick_create()

	def test_campaign_quick_create(self):
		Campaign.quick_create()

	def test_campaign_get_absolute_url(self):
		campaign = Campaign()
		campaign.pk = 123
		url = campaign.get_absolute_url()
		assert url == '/123/'



