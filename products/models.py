from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=23, decimal_places=8)
    status = models.CharField(max_length=20)
    quantity = models.PositiveBigIntegerField()

    # 참조관계는 나중에