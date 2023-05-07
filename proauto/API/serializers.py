from rest_framework import serializers
from .models import ServiceModel, WorkExampleModel, ImagesModel


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = '__all__'


class WorkExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExampleModel
        fields = '__all__'


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesModel
        fields = '__all__'
