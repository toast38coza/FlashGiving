from django.conf import settings # import the settings file
from django.contrib.sites.shortcuts import get_current_site
from django.utils.functional import SimpleLazyObject


def settings_context(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    
    return {
    	'PAYFAST_URL': settings.PAYFAST_URL,
    	'SITE': SimpleLazyObject(lambda: get_current_site(request)),
    }