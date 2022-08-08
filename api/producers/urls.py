from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import Producers_viewset

router = DefaultRouter()
router.register("", Producers_viewset, basename="producers")

urlpatterns = [

]
urlpatterns += router.urls
