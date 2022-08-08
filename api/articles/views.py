from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from api.models import Zamowienia, OpisZamowienia, Artykuly, Producenci

from .serializers import Articles_serializer
from api.producers.serializers import Producers_serializer


class Articles_viewset(viewsets.ModelViewSet):
	queryset = Artykuly.objects.all()
	serializer_class = Articles_serializer

	#override of serializer_class
	def get_serializer_context(self):

		context = super(Articles_viewset, self).get_serializer_context()
		context.update({"request": self.request})
		return context


	# POST
	def create(self, request, pk=None, *args, **kwargs):
	
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(headers=headers, status=status.HTTP_201_CREATED)
		pass
	
	def perform_create(self, instance, pk=None, *args, **kwargs):
		instance.save()
		pass

	