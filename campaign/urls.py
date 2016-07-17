from django.conf.urls import url, include
from .views import CampaignList, CampaignDetail, DonationSuccess

urlpatterns = [
    url(r'^$', CampaignList.as_view(), name='campaign_list'),
    url(r'^(?P<pk>[\w-]+)/success/$', DonationSuccess.as_view(), name='transaction_detail'),
    url(r'^(?P<slug>[\w-]+)/$', CampaignDetail.as_view(), name='campaign_detail'),
]