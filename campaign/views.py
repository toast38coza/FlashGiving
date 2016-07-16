from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Campaign, Team, Transaction

class CampaignList(ListView):
    model = Campaign
    context_object_name = 'campaign_list'

class CampaignDetail(DetailView):

    model = Campaign

    def get_context_data(self, **kwargs):

    	context = super(CampaignDetail, self).get_context_data(**kwargs)
    	
    	transaction_id = self.request.GET.get('transaction_id', None)
    	teams = Team.objects.filter(campaign=self.object.id)

    	if transaction_id:
    		transaction = Transaction.objects.get(id=transaction_id)
    		context['transaction'] = transaction
    		context['teams'] = teams

        return context