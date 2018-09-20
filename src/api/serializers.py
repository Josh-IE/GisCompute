from rest_framework import serializers

class GeoSerializer(serializers.Serializer):
    x = serializers.DecimalField(required=True, max_digits=None, decimal_places=None)
    y = serializers.DecimalField(required=True, max_digits=None, decimal_places=None)
    n = serializers.IntegerField(required=True, min_value=0)
    

    
