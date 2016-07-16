from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Campaign 


class CampaignList(ListView):
    model = Campaign
    context_object_name = 'campaign_list'

class CampaignDetail(DetailView):

    model = Campaign

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CampaignDetail, self).get_context_data(**kwargs)
        
        return context