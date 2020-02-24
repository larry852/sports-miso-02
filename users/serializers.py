from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from rest_auth.models import TokenModel

User = get_user_model()


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    def custom_signup(self, request, user):
        user.first_name = self.validated_data.get('first_name', '')
        user.last_name = self.validated_data.get('last_name', '')
        user.save(update_fields=['first_name', 'last_name'])


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'get_full_name')


class CustomTokenSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = TokenModel
        fields = ('key', 'user')
