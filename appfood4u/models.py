from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    product_name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, default='Product1')
    price = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Renamed 'name' to 'category' for clarity

    def __str__(self):
        return self.product_name
    
    
class Myimage(models.Model):
    image = models.ImageField(upload_to='images')
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Image for {self.product.product_name}" if self.product else "Image without product"

