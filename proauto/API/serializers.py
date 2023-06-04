from rest_framework import serializers
from .models import ServiceModel, WorkExampleModel, ImagesModel


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesModel
        fields = '__all__'


class WorkExampleSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(format="%d.%m.%Y", input_formats=['%d.%m.%Y', 'iso-8601'])
    end_date = serializers.DateField(format="%d.%m.%Y", input_formats=['%d.%m.%Y', 'iso-8601'])
    images = ImagesSerializer(many=True, read_only=True, source='images_set')

    class Meta:
        model = WorkExampleModel
        fields = ('id', 'service_id', 'description', 'start_date', 'end_date', 'images')


class ServiceSerializer(serializers.ModelSerializer):
    work_examples = WorkExampleSerializer(many=True, read_only=True, source='work_examples_set')

    class Meta:
        model = ServiceModel
        fields = ('id', 'title', 'min_price', 'description', 'work_examples')

