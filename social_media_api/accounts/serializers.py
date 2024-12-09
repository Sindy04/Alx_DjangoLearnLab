from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token

class UserSerializers(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'bio', 'profile_picture']

serializers.CharField()
Token.objects.create
get_user_model().objects.create_user
