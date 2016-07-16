from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from autoslug import AutoSlugField

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





class Campaign(models.Model):

    name = models.CharField(max_length=30)
    slug = AutoSlugField(populate_from='name')
    charity = models.ForeignKey(Charity)
    picture = models.URLField(blank=True, null=True)

    description = models.TextField(max_length=30, blank=True, null=True)
    raised = models.IntegerField(default=0)

    created = models.DateTimeField(default=timezone.now())
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):              # __unicode__ on Python 2
        return self.name

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
    description = models.TextField(max_length=30)
    website = models.URLField()
    

    class Meta:
        ordering = ["-name"]

    def __str__(self):              # __unicode__ on Python 2
        return self.name
