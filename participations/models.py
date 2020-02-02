from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from athletes.models import Athlete


# Create your models here.
class Participation(models.Model):
    datetime = models.DateField(null=False)
    youtube_id = models.URLField(max_length=200, null=True)
    result = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=False)

class Commentary(models.Model):
    comment = models.CharField(maxlength=200, null=False, blank=False)
    datetime = models.DateField(null=False)
