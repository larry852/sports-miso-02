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
    comentaries = serializers.SerializerMethodField()

    class Meta:
        model = Participation
        exclude = ['athlete']

    def get_comentaries(self, participation):
        sports = Commentary.objects.filter(participation=participation).distinct().all()
        serializer = CommentarySerializer(sports, many=True, context={"request": self.context.get('request')})
        return serializer.data
