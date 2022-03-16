from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet

from products.models import Product, Brand
from products.serializers import ProductSerializer, BrandSerializer


def hello_world(request):
    return HttpResponse("Hello, world. You're at the products index.")


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
