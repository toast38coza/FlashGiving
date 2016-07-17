from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Campaign, Team, Transaction
from .forms import TeamForm

class CampaignList(ListView):
    model = Campaign
    context_object_name = 'campaign_list'

class CampaignDetail(DetailView):

    model = Campaign

    def get_context_data(self, **kwargs):

        context = super(CampaignDetail, self).get_context_data(**kwargs)
        
        return context

class DonationSuccess(DetailView):

    model = Transaction

    def get_context_data(self, **kwargs):

        context = super(DonationSuccess, self).get_context_data(**kwargs)
        transaction = self.object
        campaign = self.object.campaign
        teams = Team.objects.filter(campaign=campaign)
        initial_data = {'campaign': campaign.pk}

        context['transaction'] = transaction
        context['teams'] = teams
        context['campaign'] = campaign
        context['team_form'] = TeamForm(initial=initial_data)

        return context

