from django.test import TestCase, Client

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
