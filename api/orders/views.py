from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from api.models import Zamowienia, OpisZamowienia

from .serializers import Zamowienia_serializer, OpisZamowienia_serializer


class Orders_viewset(viewsets.ModelViewSet):

	queryset = Zamowienia.objects.all()
	serializer_class = Zamowienia_serializer
	lookup_field = "id"

	#override of serializer_class
	def get_serializer_context(self):

		context = super(Orders_viewset, self).get_serializer_context()
		context.update({"request": self.request})
		return context

	#POST
	def create(self, request, pk=None, *args, **kwargs):
		print("POST POST")
		print("POST POST")
		print("POST POST")

		print(request.data)

		serializer = self.get_serializer(data=request.data)

		serializer.is_valid(raise_exception=True)
		
		# self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)

		return Response(serializer.data, headers=headers, status=status.HTTP_201_CREATED)
		pass
	
	def perform_create(self, instance, pk=None, *args, **kwargs):
		instance.save()
		pass



