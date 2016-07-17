from django.conf import settings # import the settings file
from django.contrib.sites.shortcuts import get_current_site
from django.utils.functional import SimpleLazyObject
from campaign.models import Team
import random

def get_team(request):
	
	t1, created = Team.objects.get_or_create(name='Red Team', slug='red', campaign_id=1)
	t2, created = Team.objects.get_or_create(name='Blue Team', slug='blue', campaign_id=1)
	
	team_options = [t1, t2]

	# default: get it from the get param
	team_id = request.GET.get('team', None)
	# do we have on already?
	if team_id is None:
		team_id = request.session.get('team', None)		

	# still not? assign a random one
	if team_id is None:
		team = random.choice(team_options)
	else:
		team = Team.objects.get(pk=team_id)

	request.session['team'] = team.pk
	return team

	

def settings_context(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    
    return {
    	'PAYFAST_URL': settings.PAYFAST_URL,
    	'SITE': SimpleLazyObject(lambda: get_current_site(request)),
    	'TEAM': get_team(request)
    }