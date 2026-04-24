from restframework import serializers
from django.contrib.auth.models import get_user_model

User=get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'passworod': {'write_only': True}}


    def create_user(self, validated_data):
        return User.objects.create_user(**validated_data)
