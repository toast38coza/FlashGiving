from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from campaign.models import Gateway

class Command(BaseCommand):

	def handle(self, *args, **options):
		
		for gw_key, gw_for_humans in settings.GATEWAY_BACKENDS:
			Gateway.objects.get_or_create(name=gw_key)
		