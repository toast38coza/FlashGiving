from django.core.management.base import BaseCommand, CommandError
from django.template.defaultfilters import slugify
from django.conf import settings
from campaign.models import *

class Command(BaseCommand):

	def handle(self, *args, **options):
		campaign = Campaign.quick_create()

		gateway = Gateway.objects.get_or_create(name="payfast")


	