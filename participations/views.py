from rest_framework import viewsets

from participations.models import Commentary
from participations.serializers import CommentarySerializer


class CommentaryViewSet(viewsets.ModelViewSet):
    queryset = Commentary.objects.all().order_by('id')
    serializer_class = CommentarySerializer
    http_method_names = ['post']
