from rest_framework import serializers
from .models import Seller,OldHandles
from rest_framework.serializers import ValidationError
class sellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'

    def validate_name(self,value):
        data = self.get_initial()
        if data == "elma":
            raise ValidationError("name cannot be elma")
        return value



class oldHandlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OldHandles
        fields = '__all__'