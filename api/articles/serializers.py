from djmoney.contrib.django_rest_framework import MoneyField

from rest_framework import serializers
from rest_framework.exceptions import NotFound

from api.models import Artykuly
from api.models import Producenci


from api.producers.serializers import Producers_serializer




class Articles_serializer(serializers.ModelSerializer):
	def __init__(self, *args, **kwargs):
		context = kwargs.get("context")
		super().__init__(*args, **kwargs)

	class Meta:
		model = Artykuly
		fields = ["id", "model","typ","cena","cena_promocja","opis","producenci_id"]

	producenci_id = serializers.SerializerMethodField()
	model = serializers.CharField(max_length=50)
	typ = serializers.CharField(max_length=50)
	cena = MoneyField(decimal_places=2,default=0,default_currency='PLN',max_digits=11)
	cena_promocja = MoneyField(decimal_places=2,default=0,default_currency='PLN',max_digits=11)
	opis = serializers.CharField(max_length=50)
	
	def get_producenci_id(self, obj):
		context = self.context["request"]

		if context.method == "GET":
			prod = Producenci.objects.filter(nazwa=obj.producenci_id).first()
			ret = Producers_serializer(prod)
			return ret.data
		
		elif context.method == "POST":
			prod = Producenci.objects.filter(id=context.data.get("producenci_id"))
			if not prod.exists():
				raise NotFound(detail="producenci_id not found")
				

			data = self.validated_data
			data["producenci_id"] = prod
			return Artykuly(**data).save()


			return prod

		return "dupa"

		

	def create(self, validated_data):
		return Artykuly(**validated_data)
