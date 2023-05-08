from django.shortcuts import render
from rest_framework import generics, viewsets

from .models import ServiceModel, WorkExampleModel, ImagesModel
from .serializers import ServiceSerializer, WorkExampleSerializer, ImagesSerializer


class ServiceAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer


class WorkExampleAPIView(generics.ListAPIView):
    queryset = WorkExampleModel.objects.all()
    serializer_class = WorkExampleSerializer


class ImagesAPIView(generics.ListAPIView):
    queryset = ImagesModel.objects.all()
    serializer_class = ImagesSerializer

