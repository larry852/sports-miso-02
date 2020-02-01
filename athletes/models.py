from django.db import models

# Create your models here.


class Trainer (models.Model):
    first_name = models.CharField(max_length=40, null=False, blank=False)
    last_name = models.CharField(max_length=40, null=True, blank=False)


class Athlete (models.Model):
    first_name = models.CharField(max_length=40,null=False, blank=False)
    last_name = models.CharField(max_length=40, null=True, blank=False)
    height = models.FloatField()
    birth_date = models.DateField(null=True, blank=True)
    birth_place = models.CharField(max_length=40, null=True, blank=False)
    picture_url = models.ImageField(upload_to='media', null=True)
    trainer_id = models.ForeignKey(Trainer, on_delete=models.CASCADE)