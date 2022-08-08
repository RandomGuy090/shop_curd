from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import Orders_viewset

router = DefaultRouter()
router.register("", Orders_viewset, basename="orders")

urlpatterns = [

]
urlpatterns += router.urls