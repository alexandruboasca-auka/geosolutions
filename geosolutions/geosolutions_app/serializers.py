from . import models
from rest_framework import serializers


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Point
        fields = ['pk', 'x', 'y', ]


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Search
        fields = ['pk', 'timestamp', 'search_x', 'search_y', 'operation', 'points', ]