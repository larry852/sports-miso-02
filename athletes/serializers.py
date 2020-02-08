from rest_framework import serializers
from .models import Athlete, Trainer


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ('__all__')

class AthleteSerializer(serializers.ModelSerializer):
    trainer = TrainerSerializer(read_only=True)
    class Meta:
        model = Athlete
        fields = ('__all__')

