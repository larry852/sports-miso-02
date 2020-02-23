from rest_framework import serializers
from .models import Athlete, Trainer
from sports.models import Sport
from sports.serializers import SportSerializer
from participations.models import Participation
from participations.serializers import ParticipationSerializer


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ('__all__')


class AthleteSerializer(serializers.ModelSerializer):
    trainer = TrainerSerializer(read_only=True)
    birth_place = serializers.CharField(source='get_birth_place_display')
    sports = serializers.SerializerMethodField()

    class Meta:
        model = Athlete
        fields = ('__all__')

    def get_sports(self, athlete):
        sports = Sport.objects.filter(modality__participation__athlete=athlete).distinct().all()
        serializer = SportSerializer(sports, many=True, context={"request": self.context.get('request')})
        return serializer.data


class DetailAthleteSerializer(AthleteSerializer):
    participations = ParticipationSerializer(read_only=True, many=True, source='participation_set')
