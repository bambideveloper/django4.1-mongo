from django.contrib.auth.models import User
from rest_framework import serializers

# from chat.models import Message

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"id": {"read_only": True}, "password": {"write_only": True}}

    def create(self, validate_data):
        username = validate_data["username"]
        email = validate_data["useremail"]
        password = validate_data["password"]

        user = User.objects.create_user(
            username = username,
            email = email,
            password = password,
        )

        return user
