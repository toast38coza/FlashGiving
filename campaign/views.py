from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Campaign, Team, Transaction
from .forms import TeamForm
from django.db.models import Sum, Max
from datetime import datetime

class CampaignList(ListView):
    model = Campaign
    context_object_name = 'campaign_list'

class CampaignDetail(DetailView):

    model = Campaign

    def get_context_data(self, **kwargs):

        campaign = self.object;
        transaction_id = self.request.GET.get('tid', None)
        transaction = None
        if transaction_id is not None:
            amount = self.request.GET.get('amt', 0)
            transaction = Transaction.objects.get(id=transaction_id)
            transaction.status = 'complete'
            transaction.amount = amount
            transaction.save()

        donations = Transaction.objects.filter(campaign=campaign.id, status='complete')
        aggregations = Transaction.objects.filter(campaign=campaign.id, status='complete') \
                            .aggregate(Sum('amount'), Max('amount'))
                            


        context = super(CampaignDetail, self).get_context_data(**kwargs)
        
        context['transaction'] = transaction
        context['donations'] = donations 
        context['total'] = aggregations.get('amount__sum')
        context['highest'] = aggregations.get('amount__max')
        context['now'] = datetime.now()
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

