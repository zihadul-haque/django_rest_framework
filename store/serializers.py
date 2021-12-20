#convert a model instance to to dictionary.
from decimal import Decimal
from rest_framework import serializers
from .models import Product,Collection


class CollectionSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    title=serializers.CharField(max_length=255)

class ProductSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    title=serializers.CharField(max_length=255)
    price=serializers.DecimalField(source='unit_price',max_digits=6,decimal_places=2)
    price_with_tax=serializers.SerializerMethodField(method_name='calculate_tax')
    # collection=serializers.StringRelatedField(
    #     # queryset=Collection.objects.all()
    # )
    # collection=CollectionSerializer()
    collection=serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(),view_name='collection-detail'
    )
    def calculate_tax(self,product:Product):
        return product.unit_price*Decimal(1.11)