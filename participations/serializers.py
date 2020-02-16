from .models import Participation
from rest_framework import serializers
from sports.serializers import ModalitySerializer


class ParticipationSerializer(serializers.ModelSerializer):
    modality = ModalitySerializer(read_only=True)

    class Meta:
        model = Participation
        exclude = ['athlete']
