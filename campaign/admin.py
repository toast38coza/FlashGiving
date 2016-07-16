from django.contrib import admin

from .models import *

class CharityAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'website')

class CampaignAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'raised')

class TeamAdmin(admin.ModelAdmin):
	list_display = ('name', 'description')

admin.site.register(Charity, CharityAdmin)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Team, TeamAdmin)