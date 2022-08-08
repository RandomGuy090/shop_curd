from django.contrib import admin
from django.urls import path, include

from .views import Articles_viewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", Articles_viewset, basename="orders")

urlpatterns = [
]

urlpatterns += router.urls
