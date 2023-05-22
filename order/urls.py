from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

order_route = routers.DefaultRouter()
order_route.register("order", views.OrderViewSet, basename="order")

orderv2_route = routers.DefaultRouter()
orderv2_route.register("order-v2", views.OrderV2ViewSet, basename="order-v2")

urlpatterns = [
    path("", include(order_route.urls)),
    path("", include(orderv2_route.urls)),
]