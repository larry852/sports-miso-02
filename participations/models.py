from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from athletes.models import Athlete
from core.utils.file import get_path_class
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Participation(models.Model):
    datetime = models.DateField(null=False)
    youtube_id = models.URLField(max_length=200, null=True)
    result = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=False)
    athlete_id =  models.ForeignKey('athletes.Athlete', on_delete = models.CASCADE)
#TODO: falta modality_id

class Commentary(models.Model):
    comment = models.CharField(max_length=200, null=False, blank=False)
    datetime = models.DateField(null=False)
<<<<<<< HEAD
    participation = models.ForeignKey('Participation', on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
=======
    participation_id = models.ForeignKey('Participation', on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
>>>>>>> 6c99e6b81125b349919b9cb3a62b692357b8d8e3
