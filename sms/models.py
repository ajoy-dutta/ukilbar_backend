from django.db import models
from person.models import Advocate

class Case(models.Model):
    title = models.CharField(max_length=200)
    advocate = models.ForeignKey(Advocate, on_delete=models.SET_NULL, null=True, related_name='cases')
