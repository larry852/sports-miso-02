from django.db import models
from core.utils.file import get_path_class


class Trainer (models.Model):
    first_name = models.CharField(max_length=40, null=False, blank=False)
    last_name = models.CharField(max_length=40, null=True, blank=False)

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return '{} - {}'.format(self.id, self.get_full_name())


class Athlete (models.Model):
    first_name = models.CharField(max_length=40, null=False, blank=False)
    last_name = models.CharField(max_length=40, null=True, blank=False)
    height = models.FloatField()
    weight = models.FloatField()
    birth_date = models.DateField(null=True, blank=True)
    birth_place = models.CharField(max_length=40, null=True, blank=False)
    picture = models.ImageField(upload_to=get_path_class, default='default-profile.png')
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return '{} - {}'.format(self.id, self.get_full_name())
