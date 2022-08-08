from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from api.models import Producenci

from .serializers import Producers_serializer


class Producers_viewset(viewsets.ModelViewSet):
	queryset = Producenci.objects.all()
	serializer_class = Producers_serializer

	#POST
	def create(self, request, pk=None, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)

		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, headers=headers, status=status.HTTP_201_CREATED)
		pass
	
	def perform_create(self, instance, pk=None, *args, **kwargs):
		instance.save()
		pass

	#PUT
	def update(self, request, pk=None, *args, **kwargs):
		instance = self.get_object()
		instance.id = pk

		serializer = self.get_serializer(instance, data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_update(serializer)

		return Response(status=status.HTTP_200_OK)
		pass

	def perform_update(self, instance, pk=None, *args, **kwargs):
		instance.save()
		pass

