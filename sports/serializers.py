from rest_framework import serializers
from .models import Sport, Modality


class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ('__all__')


class ModalitySerializer(serializers.ModelSerializer):
    sport = SportSerializer(read_only=True)

    class Meta:
        model = Modality
        fields = ('__all__')
