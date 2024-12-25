from rest_framework import serializers
from clothes.models import Cloth

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloth
        fields = '__all__'