from django.db import models


# Create your models here.
class Investor(models.Model):
    investor = models.CharField(max_length=100)
    amount = models.FloatField()
    equity = models.FloatField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.investor

    # order by created_at
    class Meta:
        ordering = ["-id"]
