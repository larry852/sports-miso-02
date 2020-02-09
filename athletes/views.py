from rest_framework import viewsets
from .models import Athlete
from .serializers import AthleteSerializer


class AthleteViewSet(viewsets.ModelViewSet):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    http_method_names = ['get']
