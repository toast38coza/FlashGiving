from django.core.management.base import BaseCommand, CommandError
import csv
from django.template.defaultfilters import slugify
from campaign.models import *

class Command(BaseCommand):

	def handle(self, *args, **options):
		Campaign.quick_create()