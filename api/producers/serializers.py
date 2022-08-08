from rest_framework import serializers
from api.models import Producenci
from django.http import JsonResponse

class Producers_serializer(serializers.Serializer):
	
	# url = serializers.URLField(max_length=50)
	# nazwa = serializers.CharField(max_length=50)

	url = serializers.URLField(max_length=50, required=False, allow_null=True)
	nazwa = serializers.CharField(max_length=50, required=False, allow_null=True)



	class Meta:
		model = Producenci
		fields = ("id","nazwa", "url")
		# fields = "__all__"

	def create(self, validated_data):
		return Producenci.objects.create( **validated_data)

	def update(self, instance, validated_data):
		instance.id = instance.pk
		instance.nazwa = validated_data.get("nazwa")
		instance.url = validated_data.get("url")

		instance.save()
		return instance

		# return Klienci.objects.all()

