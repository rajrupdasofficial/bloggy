from django.shortcuts import render
from rest_framework import serializers
from rest_framework import generics

class Indexview(generics.ListAPIView):
    model = ''
    serializer_class=''
    template_name = ''


