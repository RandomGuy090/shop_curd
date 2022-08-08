from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path("articles/", include("api.articles.urls")),
    path("clients/", include("api.clients.urls")),
    path("orders/", include("api.orders.urls")),
    path("producers/", include("api.producers.urls"))
]
