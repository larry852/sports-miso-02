from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from athletes.models import Athlete
from core.utils.file import get_path_class
from core.utils.datetime import datetime_format
from django.contrib.auth import get_user_model

User = get_user_model()


class Participation(models.Model):
    datetime = models.DateTimeField(null=False)
    youtube_id = models.CharField(max_length=200, null=False)
    result = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=False)
    athlete = models.ForeignKey('athletes.Athlete', on_delete=models.CASCADE)
    modality = models.ForeignKey('sports.Modality', on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {} ({})'.format(self.id, datetime_format(self.datetime), self.athlete.get_full_name())


class Commentary(models.Model):
    comment = models.CharField(max_length=200, null=False, blank=False)
    datetime = models.DateTimeField(null=False)
    participation = models.ForeignKey('Participation', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}... ({})'.format(self.id, self.comment[:5], self.user.username)
