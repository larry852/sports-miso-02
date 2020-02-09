from rest_framework import viewsets
from .models import Athlete
from .serializers import AthleteSerializer


class AthleteViewSet(viewsets.ModelViewSet):
    queryset = Athlete.objects.all().order_by('id')
    serializer_class = AthleteSerializer
    http_method_names = ['get']
