
from django.conf.urls import url, include
from django.contrib import admin
from campaign.api import router

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^api/', include(router.urls)),
	url(r'^', include('campaign.urls')),
]
