from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import ServiceModel, WorkExampleModel, ImagesModel
from .serializers import ServiceSerializer, WorkExampleSerializer, ImagesSerializer


class ServiceAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = ServiceModel.objects.all()
    serializer_class = ServiceSerializer

    @action(methods=['get'], detail=True)
    def work_examples(self, request, pk=None):
        queryset = WorkExampleModel.objects.filter(service_id=pk)
        serializer = WorkExampleSerializer(queryset, many=True)
        return Response({'work_examples': serializer.data if serializer.data else [{'description':'В данный момент примеры работ отсутсвуют.'}]})


class WorkExampleAPIView(generics.ListAPIView):
    queryset = WorkExampleModel.objects.all()
    serializer_class = WorkExampleSerializer


class ImagesAPIView(generics.ListAPIView):
    queryset = ImagesModel.objects.all()
    serializer_class = ImagesSerializer

