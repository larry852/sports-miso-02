from rest_framework import viewsets

from .models import Sport, Modality
from .serializers import SportSerializer, ModalitySerializer


class SportViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.all().order_by('id')
    serializer_class = SportSerializer
    http_method_names = ['get']


class ModalityViewSet(viewsets.ModelViewSet):
    queryset = Modality.objects.all().order_by('id')
    serializer_class = ModalitySerializer
    http_method_names = ['get']
    filter_fields = ['sport']
