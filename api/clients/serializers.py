from rest_framework import serializers
from api.models import Klienci
from django.http import JsonResponse

class Client_serializer(serializers.ModelSerializer):
	# id = serializers.IntegerField(required=False)
	# nazwa = serializers.CharField(max_length=50)
	# adres = serializers.CharField(max_length=50)
	# nip = serializers.CharField(max_length=10)

	class Meta:
		model = Klienci
		fields = ("id","nazwa", "adres", "nip")
		# fields = "__all__"

	def create(self, validated_data):
		return Klienci.objects.create( **validated_data)

	def update(self, instance, validated_data):
		instance.id = instance.pk
		instance.nazwa = validated_data.get("nazwa")
		instance.adres = validated_data.get("adres")
		instance.nip = validated_data.get("nip")

		instance.save()
		return instance

		# return Klienci.objects.all()

	def delete(self, instance):
		print("serializer delete")

	def validate(self, data):
		print(f"client_serializer validation {data}")
		return data