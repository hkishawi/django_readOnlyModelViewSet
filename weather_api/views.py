from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DescriptionSerializer
from .models import Description

# Create your views here.

class DescriptionViewSet(viewsets.ReadOnlyModelViewSet):
    """create weather descriptions and read the info"""
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer