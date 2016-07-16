from rest_framework import routers, serializers, viewsets
from .models import Team, Campaign

# Serializers define the API representation.
class CampaignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Campaign
        fields = ('name',)

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer   



# Serializers define the API representation.
class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer   

router = routers.DefaultRouter()
router.register(r'campaigns', CampaignViewSet)  
router.register(r'teams', TeamViewSet)         