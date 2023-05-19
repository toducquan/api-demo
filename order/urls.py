from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

order_route = routers.DefaultRouter()
order_route.register("order", views.OrderViewSet, basename="order")

urlpatterns = [
    path("", include(order_route.urls)),
]