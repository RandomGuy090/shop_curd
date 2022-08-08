from django.contrib import admin
from django.urls import path, include

from .views import ClientViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", ClientViewset, basename="client")

urlpatterns = [
]

urlpatterns += router.urls
