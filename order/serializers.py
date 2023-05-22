
from rest_framework import serializers
from . import models
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = "__all__"

class OrderV2Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderV2
        fields = "__all__"
