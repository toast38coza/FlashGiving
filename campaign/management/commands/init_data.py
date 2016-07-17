from django.core.management.base import BaseCommand, CommandError
from django.template.defaultfilters import slugify
from django.conf import settings
from campaign.models import *

class Command(BaseCommand):

	def handle(self, *args, **options):
		campaign = Campaign.quick_create()

		# teams:
		red = Team()
		red.name = "Read Team"
		red.campaign = campaign
		red.save()

		blue = Team()
		blue.name = "Read Team"
		blue.campaign = campaign
		blue.save()


	