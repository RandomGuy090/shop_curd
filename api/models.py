from django.db import models
from djmoney.models.fields import MoneyField


# Create your models here.



class Klienci(models.Model):
	nazwa = models.CharField(max_length=50)
	adres = models.CharField(max_length=50)
	nip = models.CharField(max_length=10)

	def __str__(self):
		return f"{self.nazwa} {self.adres} {self.nip}"

class Zamowienia(models.Model):
	ORDER_CHOICES = (
		("Order placed","Order placed"),
		("Order received","Order received"),
		("Products Picked","Products Picked"),
		("Order shipped","Order shipped"),
		("Order delivered","Order delivered")
		)


	nazwa = models.CharField(max_length=50)
	klientID = models.ForeignKey("Klienci", on_delete=models.CASCADE)
	status = models.CharField(max_length=50, choices=ORDER_CHOICES)
	data = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	nr_faktury = models.CharField(max_length=50)
	

	# opis_zamowienia_id = models.ForeignKey("OpisZamowienia",related_name="opis_zamowienia_id" , on_delete=models.CASCADE)


	def __str__(self):
		return f"order nr: {self.id}"

class Producenci(models.Model):
	nazwa = models.CharField(max_length=50)
	url = models.CharField(max_length=50)

	def __str__(self):
		return f"{self.nazwa}"

class Artykuly(models.Model):
	zamowienia_id = models.ForeignKey("Zamowienia", on_delete=models.CASCADE)
	producenci_id = models.ForeignKey("Producenci", on_delete=models.CASCADE)
	
	model = models.CharField(max_length=50)
	typ = models.CharField(max_length=50)
	cena = MoneyField(decimal_places=2,default=0,default_currency='PLN',max_digits=11)
	cena_promocja = MoneyField(decimal_places=2,default=0,default_currency='PLN',max_digits=11)

	opis = models.CharField(max_length=50)

	def __str__(self):
		return f"{self.model}"
	

class OpisZamowienia(models.Model):
	zamowienia_id = models.ForeignKey("Zamowienia",related_name="zamowienia_id" , on_delete=models.CASCADE)
	artykuly_id = models.ForeignKey("Artykuly", related_name="artykuly_id", on_delete=models.CASCADE)
	ilosc = models.IntegerField()
	opis = models.CharField(max_length=250)

	def __str__(self):
		return f"{self.opis[0:20]}"



