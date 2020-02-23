from rest_framework import serializers

from sports.serializers import ModalitySerializer
from .models import Participation, Commentary


class CommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentary
        fields = ('__all__')
        read_only_fields = ['datetime']


class ParticipationSerializer(serializers.ModelSerializer):
    modality = ModalitySerializer(read_only=True)
    commentaries = CommentarySerializer(read_only=True, many=True, source="commentary_set")

    class Meta:
        model = Participation
        exclude = ['athlete']
