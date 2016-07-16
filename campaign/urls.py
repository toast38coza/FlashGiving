from django.conf.urls import url
from .views import CampaignList, CampaignDetail

urlpatterns = [
    url(r'^$', CampaignList.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', CampaignDetail.as_view()),
]