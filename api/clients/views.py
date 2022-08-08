from api.models import Klienci

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import Client_serializer

class ClientViewset(viewsets.ModelViewSet):
	queryset = Klienci.objects.all()
	serializer_class = Client_serializer

	#POST
	def create(self, request, pk=None, *args, **kwargs):

		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)

		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

	def perform_create(self, instance, pk=None):
		instance.save()
		pass

	#DELETE
	def destroy(self, request, pk=None, *args, **kwargs):
		instance = self.get_object()
		self.perform_destroy(instance)

		return Response(status=status.HTTP_204_NO_CONTENT)

	def perform_destroy(self, instance, pk=None):
		instance.delete()

	#PUT
	def update(self, request, pk=None, *args, **kwargs):

		instance = self.get_object()
		instance.id = pk
		serializer = self.get_serializer(instance, data=request.data)

		serializer.is_valid(raise_exception=True)

		self.perform_update(serializer)

		return Response(status=status.HTTP_200_OK)

	def perform_update(self, instance):
		instance.save()

	@action(detail=True, methods=["GET"])
	def info(self, request, pk=None):

		qr = self.get_queryset()
		res = {"status": 200,
				"code": "dupa"}
		return Response(res)















