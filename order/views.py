from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import (
    serializers,
    models,
)
# Create your views here.

class OrderViewSet(ModelViewSet):
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()