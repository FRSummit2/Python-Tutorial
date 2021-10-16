from rest_framework import serializers
from .models import DeliveryPlan

class DeliveryPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryPlan
        fields = '__all__'
