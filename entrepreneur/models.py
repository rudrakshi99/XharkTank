from django.db import models

from investor.models import Investor


class Entrepreneur(models.Model):
    entrepreneur = models.CharField(max_length=100, blank=True)
    pitchTitle = models.CharField(max_length=100, blank=True)
    pitchIdea = models.TextField(blank=True)
    askAmount = models.FloatField(blank=True)
    equity = models.FloatField(blank=True)
    offers = models.ManyToManyField(Investor, related_name="offers", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.entrepreneur

    class Meta:
        ordering = ["-id"]
