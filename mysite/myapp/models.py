from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='images')

    def __str__(self):
        return self.name