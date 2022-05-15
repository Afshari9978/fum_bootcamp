import random

from django.core.management.base import BaseCommand

from products.models import Brand, Category, Product


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        for i in range(500):
            brands = [Brand(name=f'Brand {i}') for i in range(1000)]
            Brand.objects.bulk_create(brands)
            categories = [Category(name=f'Cat {i}') for i in range(1000)]
            Category.objects.bulk_create(categories)
            products = [Product(
                name=f'Book {i}-{j}',
                brand_id=random.randint(1, 11),
                category_id=random.randint(1, 11),
            ) for j in range(1000 * 2)]
            Product.objects.bulk_create(products)

            self.stdout.write(self.style.SUCCESS(i))
