from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    products = models.ManyToManyField('Product', blank=True)


class Brand(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    icon = models.ImageField(blank=True)


class BrandPrize(models.Model):
    brand = models.OneToOneField(Brand, on_delete=models.CASCADE)
    product = models.OneToOneField('Product', on_delete=models.SET_NULL, null=True, blank=True)
    date_effective_start = models.DateTimeField(blank=True, null=True)
    date_effective_end = models.DateTimeField(blank=True, null=True)


class Category(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    main_photo = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    quantity = models.IntegerField(blank=True, default=1, null=True)

    date_created = models.DateTimeField(
        auto_now_add=True,
    )
    date_updated = models.DateTimeField(
        auto_now=True
    )


class ProductPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=2.5)
    discount = models.FloatField(default=0)
    date_effective_start = models.DateTimeField(blank=True, null=True)
    date_effective_end = models.DateTimeField(blank=True, null=True)


class Cart(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    date_created = models.DateTimeField(auto_now_add=True)
