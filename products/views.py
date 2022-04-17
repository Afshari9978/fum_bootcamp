from django.http import HttpResponse
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from products.models import Product, Brand
from products.serializers import ProductSerializer, BrandSerializer


def hello_world(request):
    return HttpResponse("Hello, world. You're at the products index.")


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.action.startswith('public_'):
            queryset = queryset.filter(category__is_public=True, is_deleted=False).select_related('category')
        if 'last_' in self.action:
            queryset = queryset.filter(quantity__lte=5)
        if self.action == 'search':
            key = self.request.query_params['key']
            queryset = queryset.filter(name__icontains=key) | queryset.filter(search_keys__icontains=key) | \
                       queryset.filter(category__name__icontains=key)

        return queryset

    def perform_destroy(self, instance):
        if self.action == 'public_delete':
            instance.is_deleted = True
            instance.save()
        else:
            super().perform_destroy(instance)

    @action(detail=False)
    def public_last_products(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @action(detail=False)
    def public_list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @action(detail=False)
    def search(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @action(methods=['delete'], detail=True)
    def public_delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
