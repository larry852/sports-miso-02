from rest_framework import viewsets

from athletes.models import Athlete
from athletes.serializers import AthleteSerializer


class AthleteViewSet(viewsets.ModelViewSet):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    http_method_names = ['get']
