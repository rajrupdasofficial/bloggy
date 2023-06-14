from .models import UserProfile
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    profile_image = serializers.ImageField()
    bio = serializers.CharField()
    password = serializers.CharField(write_only=True)
    # Add other fields as needed

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'bio', 'profile_image')  # Add other fields as needed
        extra_kwargs = {
            'field1': {'required': False},
            'field2': {'required': False},
            # Add extra kwargs for other fields as needed
        }

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        password = user_data.pop('password')
        user = User.objects.create_user(**user_data)
        user.set_password(password)
        user.save()

        profile = UserProfile.objects.create(user=user, **validated_data)
        return profile

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        password = user_data.get('password')
        if password:
            instance.user.set_password(password)
        for attr, value in user_data.items():
            setattr(instance.user, attr, value)
        instance.user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
