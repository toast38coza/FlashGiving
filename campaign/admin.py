from django.contrib import admin

from .models import *

class GatewayPropertyInline(admin.TabularInline):
	model = GatewayProperty 

class CharityAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'website')
	inlines = [GatewayPropertyInline]

class CampaignAdmin(admin.ModelAdmin):
	list_display = ('name', 'description')

class TeamAdmin(admin.ModelAdmin):
	list_display = ('name', 'description')



admin.site.register(Charity, CharityAdmin)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Team, TeamAdmin)