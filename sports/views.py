from rest_framework import viewsets

from .models import Sport
from .serializers import SportSerializer


class SportViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.all().order_by('id')
    serializer_class = SportSerializer
    http_method_names = ['get']
