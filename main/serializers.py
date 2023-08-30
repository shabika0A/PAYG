from rest_framework import serializers

class CostSerializer(serializers.Serializer):
    username = serializers.CharField()
    current_month = serializers.IntegerField()
    request_count=serializers.IntegerField()
    cost = serializers.DecimalField(max_digits=10, decimal_places=3)