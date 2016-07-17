from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.conf import settings
from autoslug import AutoSlugField
from django.core.urlresolvers import reverse

import json, uuid

class Charity(models.Model):

    name = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='name')
    description = models.TextField(max_length=30, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    
    class Meta:
        ordering = ["-name"]

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    @staticmethod 
    def quick_create(name=None):

        if name is None: name = "Ubunye Foundation"

        data = {
            "name": name        
        }

        return Charity.objects.create(**data)

    @property
    def gateway_properties(self):
        vals = self.gatewayproperty_set.all().values()
        return {item.get('key'): item.get('value') for item in vals}
    
    
class GatewayProperty(models.Model):
    
    charity = models.ForeignKey(Charity)
    gateway_name = models.CharField(max_length=30, default='payfast', choices=settings.GATEWAY_BACKENDS)    
    key = models.CharField(max_length=30)
    value = models.CharField(max_length=255, blank=True, null=True)


CAMPAIGN_STATES = [('pending', 'Pending'), ('active', 'Active'), ('complete', 'Complete'), ('cancelled', 'Cancelled')]

class Campaign(models.Model):

    name = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='name')
    charity = models.ForeignKey(Charity)
    picture = models.URLField(blank=True, null=True)

    description = models.TextField(max_length=30, blank=True, null=True)
    raised = models.IntegerField(default=0)
    status = models.CharField(max_length=30, choices=CAMPAIGN_STATES, default='pending')

    expiry_date = models.DateTimeField(blank=True, null=True)

    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('campaign_detail', args=[self.pk])

    def get_active(self):
        return Campaign.objects.filter(status='active')

    @staticmethod
    def quick_create(charity=None, name=None, picture=None):

        if name is None: name = "Mandela Day Challenge"
        if picture is None: picture = "http://www.gatesfoundation.org/~/media/GFO/Home/banner-1.png"
        if charity is None:
            if Charity.objects.count() > 0:
                charity = Charity.objects.first()
            else:
                charity = Charity.quick_create()                

        data = {
            "name": name,
            "picture": picture,
            "charity": charity
        }
        return Campaign.objects.create(**data)

class Team(models.Model):

    campaign = models.ForeignKey(Campaign)
    name = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='name')
    description = models.TextField(max_length=30, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    avatar = models.URLField(blank=True, null=True)
    
    class Meta:
        ordering = ["-name"]

    def __str__(self):              # __unicode__ on Python 2
        return self.name

transaction_statuses = [('started', 'Started'), ('complete', 'Complete')]
class Transaction(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    campaign = models.ForeignKey(Campaign)
    team = models.ForeignKey(Team, blank=True, null=True)
    amount = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=30, choices=transaction_statuses, default='started')





