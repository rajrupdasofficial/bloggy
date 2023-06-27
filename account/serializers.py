from rest_framework import serializers
from account.models import User
from django.contrib.auth.hashers import make_password
from django.utils.encoding import smart_str, force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import DjangoUnicodeDecodeError
from .utils import Util
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth import authenticate, login
import re

class UserRSerializer(serializers.HyperlinkedModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')

        if password != password2:
            raise serializers.ValidationError("Passwords do not match")

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user
    def validate_email(self, value):
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError("Invalid email format")

        return value
    
    def  validate_password(self, value):
    # Minimum length check
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long")

    # Character complexity check
        if not re.search(r'[A-Z]', value) or not re.search(r'[a-z]', value) or not re.search(r'\d', value) or not re.search(r'[!@#$%^&*]', value):
            raise serializers.ValidationError("Password must include at least one uppercase letter, one lowercase letter, one digit, and one special character")

    # Commonly used passwords check
        weak_passwords = ['password', '123456', 'qwerty', ...]  # List of weak passwords
        if value in weak_passwords:
            raise serializers.ValidationError("Password is too weak. Please choose a stronger password")

        return value



class UserLSerializer(serializers.HyperlinkedModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email','password']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields =['id','email','name']

#password change serializer
class PasChSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True)
    password2 = serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True)
    class Meta:
        fields = ['password','password2']
    def validate(self, attrs):
        password = attrs.get('password')
        print(password)
        password2 = attrs.get('password2')
        print(password2)
        user = self.context.get('user')
        print(user)
        if password!=password2:
            raise serializers.ValidationError('Passwords wont match')
        user.set_password(password)
        user.save()
        return super().validate(attrs)

# send password reset email service with token
class SPS(serializers.Serializer):
    email =  serializers.EmailField(max_length=255)
    class Meta:
        fields = ['email']
    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print('Encoded uid',uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print("reset token",token)
            link = 'http://localhost:8000/api/user/reset/'+uid+'/'+token
            print('link',link)
            # send email
            body = 'Click the link to proceed'+link
            data = {
               'subject':'Reset password',
               'body':body,
               'to_email':user.email,

            }
            Util.send_email(data)
            return super().validate(attrs)
        else:
            raise serializers.ValidationError('you are not a register user')


#user password reset serializer
class UPRS(serializers.Serializer):
    password = serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True)
    password2 = serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True)
    class Meta:
        fields = ['password','password2']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            password2 = attrs.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')
            if password!=password2:
                raise serializers.ValidationError('Passwords wont match')
            id = smart_str (urlsafe_base64_decode(uid))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise serializers.ValidationError('token didnot match or expired')
            user.set_password(password)
            user.save()
            return super().validate(attrs)
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user,token)            
            raise serializers.ValidationError('token didnot match or expired')
