from rest_framework.serializers import ModelSerializer, SerializerMethodField

from products.models import Product, Brand


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    brand_name = SerializerMethodField()
    category_name = SerializerMethodField()

    def get_brand_name(self, obj):
        return obj.brand.name

    def get_category_name(self, obj):
        return obj.category.name


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
