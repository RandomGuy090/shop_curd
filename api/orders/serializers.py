from rest_framework import serializers
from api.models import Zamowienia, OpisZamowienia, Artykuly, Klienci


from api.clients.serializers import Client_serializer
from api.articles.serializers import Articles_serializer





class OpisZamowienia_serializer(serializers.ModelSerializer):
	art_list = dict()
	artykuly_id = Articles_serializer()
	

	class Meta:
		model = OpisZamowienia
		fields = ("id", "artykuly_id", "ilosc", "opis")


	def get_artykuly_id(self, obj):
		
		try:
			isinstance(self.art_list[int(obj.zamowienia_id.id)], list)
		except KeyError:
			self.art_list[obj.zamowienia_id.id] = []

		qr = Artykuly.objects.filter(id=obj.artykuly_id.id)

		parsed = Articles_serializer(qr, context=self.context, many=True).data

		self.art_list[obj.zamowienia_id.id].append(parsed[0])

		if self.art_list.get(int(obj.id)):
			return self.art_list.get(int(obj.id))
		else: 
			return ""

	
def validators(value):
	print(f"custom validation function: {value}")


class Zamowienia_serializer(serializers.Serializer):


	nazwa = serializers.CharField(max_length=50)
	status = serializers.CharField(max_length=50)
	data = serializers.DateTimeField(allow_null=True, required=False)
	nr_faktury = serializers.CharField(max_length=50)
	
	# klientID = Client_serializer()
	# klientID = serializers.SerializerMethodField()
	elements = serializers.SerializerMethodField()
	
	# class Meta:
	# 	model = Zamowienia
	# 	fields = ("id", "nazwa","klientID", "status", "data", "nr_faktury", "opis_zamowienia_id")


	def get_elements(self, obj):
		context = self.context.get("request")
		field_val = self.context.get('request').data.get("elements")
		print(context)

		if context.method == "GET":
			art_list = {}		
			qr = OpisZamowienia.objects.filter(zamowienia_id = obj.id)
			ser = OpisZamowienia_serializer(qr, context=self.context, many=True).data
			
			for elem in ser:
				art_list[len(art_list)+1] = elem

			ret  = art_list
			return ret

		elif context.method == "POST":
			print(f"context post {field_val}")
			
			art_list = []
			for elem in field_val:
				qr = OpisZamowienia.objects.filter(id=elem)
				print(qr)
				ser = OpisZamowienia_serializer(qr, context=self.context, many=True).data
				print(ser)
				art_list.append(ser)

			print(art_list)
			print(art_list)
			# return OpisZamowienia_serializer(art_list)
			return art_list



	def get_klientID(self, obj):
		context = self.context.get("request")

		if context.method == "GET":
			qr = Klienci.objects.filter(id=obj.klientID.id).first()
			ser = Client_serializer(qr, context=self.context).data
			return ser

		elif context.method == "POST":
			print(f"print klient id: {obj}")


	def validate_klientID(self, data):
		print(f"validation {data}")
		print(f"validation {data}")
		print(f"validation {data}")
		return data


	def create(self, validated_data):
		print(validated_data)
		# return Klienci


