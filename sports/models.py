from django.db import models
from core.utils.file import get_path_class


class Modality(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    sport = models.ForeignKey('Sport', on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.id, self.name)


class Sport(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    icon = models.ImageField(upload_to=get_path_class, default='default-sport.png')

    def __str__(self):
        return '{} - {}'.format(self.id, self.name)
