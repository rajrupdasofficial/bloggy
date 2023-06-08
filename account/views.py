from rest_framework.views import APIView
from .serializers import UserRSerializer, UserLSerializer, ProfileSerializer,PasChSerializer,SPS, UPRS
from django.contrib.auth import authenticate
from .renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth import authenticate, login


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    payload = refresh.payload

    # Remove the 'user_id' field from the payload
    payload.pop('user_id', None)

    # Add 'uid' to the token payload as a string
    payload['uid'] = str(user.uid)

    # Reconstruct the refresh token with the updated payload
    refresh.payload = payload

    return {'refresh': str(refresh), 'access': str(refresh.access_token)}



# Decorators for security measures
csrf_protect_m = method_decorator(csrf_protect)
never_cache_m = method_decorator(never_cache)
sensitive_post_parameters_m = method_decorator(sensitive_post_parameters())
#user registration 
class Registration(APIView):
    renderer_classes = [UserRenderer]
    
    @csrf_protect_m
    @never_cache_m
    def post(self, request, format=None):
        reg_serializer = UserRSerializer(data=request.data)
        if reg_serializer.is_valid(raise_exception=True):
            user = reg_serializer.save()
            tokens = get_tokens_for_user(user)
            refresh_token = tokens['refresh']
            access_token = tokens['access']

            response = Response({'token': access_token, 'msg': 'User registration successful'}, status=status.HTTP_201_CREATED)

            # Set the refresh token as an HTTP-only cookie
            response.set_cookie('refresh_token', refresh_token, httponly=True, samesite='None', secure=True)

            return response
        else:
            # Check if username or email already exists in the errors
            if 'username' in reg_serializer.errors and 'email' in reg_serializer.errors:
                error_message = 'Username and email are already registered. Please login.'
            elif 'username' in reg_serializer.errors:
                error_message = 'Username is already registered. Please choose a different username.'
            elif 'email' in reg_serializer.errors:
                error_message = 'Email is already registered. Please use a different email.'
            else:
                error_message = 'Registration failed.'

            return Response({'msg': error_message}, status=status.HTTP_400_BAD_REQUEST)


def is_password_strong(password):
    # Implement your own password strength validation logic here
    # Return True if the password is strong enough, False otherwise
    # You can include requirements such as minimum length, character complexity, etc.
    # Example implementation:
    return len(password) >= 8

#user login section
# user login section
class Login(APIView):
    renderer_classes = [UserRenderer]
    
    @csrf_protect_m
    @never_cache_m
    def post(self, request, format=None):
        serializer = UserLSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            print('password',password)
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)  # Logs the user in and creates a session
                # Generate the token
                token = get_tokens_for_user(user)
                # Set the token as an HTTP-only session cookie
                response = Response({'token': token, 'msg': 'Success Login'})
                response.set_cookie('refresh_token', token['refresh'], httponly=True, samesite='Strict')
                return response
            else:
                print('User authentication failed:', email,password)
                
                return Response({'errors': {'non_field_errors': ['Email or password is not valid.']}}, status=400)
        else:
            print('Serializer validation failed:', serializer.errors)
            return Response({'errors': serializer.errors}, status=400)
