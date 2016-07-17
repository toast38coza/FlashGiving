from rest_framework import routers, serializers, viewsets, filters, fields, permissions
from .models import Team, Campaign, Transaction

# TODO: Sort out the permissions properly


# Serializers define the API representation.
class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ('name',)

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer   

# Serializers define the API representation.
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer  
    

class TransactionFilter(filters.FilterSet):
    class Meta:
        model = Transaction
        fields = ['campaign', 'team', 'status']

class TransactionSerializer(serializers.ModelSerializer):
    id = fields.CharField(read_only=True)
    amount = fields.IntegerField(read_only=True)
    status = fields.CharField(read_only=True)
    class Meta:
        model = Transaction
        
        
class TransactionViewSet(viewsets.ModelViewSet):
    """
    Note: transaction_id, amount and status are read only
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer  
    filter_class = TransactionFilter


router = routers.DefaultRouter()
router.register(r'campaigns', CampaignViewSet)  
router.register(r'teams', TeamViewSet)         
router.register(r'transactions', TransactionViewSet)         