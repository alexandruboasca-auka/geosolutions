from . import models, serializers, lib
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class PointViewSet(viewsets.ModelViewSet):
	queryset = models.Point.objects.all()
	serializer_class = serializers.PointSerializer

class SearchViewSet(viewsets.ModelViewSet):
	queryset = models.Search.objects.all().order_by('-timestamp')
	serializer_class = serializers.SearchSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)

		point_queryset = models.Point.objects.all()
		point_serializer = serializers.PointSerializer(point_queryset, many=True)

		data = point_serializer.data
		points = []

		for p in data:
			points.append((p['x'], p['y']))

		result_points = lib.find_points(
			points,
			(serializer.validated_data['search_x'], serializer.validated_data['search_y']),
			serializer.validated_data['points'],
			serializer.validated_data['operation']
		)

		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(result_points, status=status.HTTP_201_CREATED, headers=headers)
