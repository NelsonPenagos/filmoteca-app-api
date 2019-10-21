from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    """UserSerializer model user"""
    user_id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length=50)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)

    def create(self, request):
        """Create user"""
        instance = User()
        instance.email = request.get('email')
        instance.username = request.get('username')
        instance.set_password(request.get('password'))
        instance.first_name = request.get('first_name')
        instance.last_name = request.get('last_name')
        instance.save()
        return instance

    def validate_username(self, data):
        """validate username exist"""
        user = User.objects.filter(username=data)
        if len(user) != 0:
            raise serializers.ValidationError("Ya existe")
        else:
            return data
