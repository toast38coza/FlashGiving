from django.db import models
from django.utils import timezone

class Charity(models.Model):

    name = models.CharField(max_length=30)
    slug = models.SlugField()
    description = models.TextField(max_length=30)
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Campaign(models.Model):

    name = models.CharField(max_length=30)
    slug = models.SlugField()
    description = models.TextField(max_length=30)
    raised = models.IntegerField()

    created = models.DateTimeField(default=timezone.now())
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Team(models.Model):

    name = models.CharField(max_length=30)
    slug = models.SlugField()
    description = models.TextField(max_length=30)
    website = models.URLField()
    

    class Meta:
        ordering = ["-name"]

    def __str__(self):              # __unicode__ on Python 2
        return self.name
