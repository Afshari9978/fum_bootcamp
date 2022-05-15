import random

from celery import shared_task

from products.models import Product


@shared_task
def add(x, y):
    products = [Product(
        name=f'Book ?',
        brand_id=random.randint(1, 11),
        category_id=random.randint(1, 11),
    ) for _ in range(1000)]
    Product.objects.bulk_create(products)
    return x + y
