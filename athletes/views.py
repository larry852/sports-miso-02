from rest_framework import viewsets
from .models import Athlete
from .serializers import AthleteSerializer, DetailAthleteSerializer
from .paginations import AthletePagination


class AthleteViewSet(viewsets.ModelViewSet):
    queryset = Athlete.objects.all().distinct().order_by('id')
    serializer_class = AthleteSerializer
    detail_serializer_class = DetailAthleteSerializer
    http_method_names = ['get']
    filter_fields = ['participation__modality__sport', 'participation__modality']
    pagination_class = AthletePagination

    def get_serializer_class(self):
        if self.action == 'retrieve':
            if hasattr(self, 'detail_serializer_class'):
                return self.detail_serializer_class
        return self.serializer_class
