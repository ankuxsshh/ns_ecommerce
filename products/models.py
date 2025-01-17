from django.db import models

TYPE_CHOICES = (
    ("Cashew", "Cashew"),
    ("Almond", "Almond"),
    ("Cardamom", "Cardamom"),
    ("Combo", "Combo"),
)

AVAILABILITY_CHOICES = (
    ("In Stock", "In Stock"),
    ("Out of Stock", "Out of Stock"),
)

class Product(models.Model):
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, null=True, blank=True)
    title = models.CharField(max_length=150, null=False, blank=False, default="")
    description = models.TextField(null=True, blank=True)  # Changed to TextField for better support of long text
    specification = models.TextField(null=True, blank=True)  # Changed to TextField for better support of long text

    def __str__(self):
        return self.title

class ProductQuantity(models.Model):
    product = models.ForeignKey(Product, related_name='quantities', on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50, choices=[('250g', '250g'), ('500g', '500g')])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.CharField(max_length=50, choices=AVAILABILITY_CHOICES, default="In Stock")

    def __str__(self):
        return f"{self.product.title} - {self.quantity}"

class ProductImage(models.Model):
    product_quantity = models.ForeignKey(ProductQuantity, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f"Image for {self.product_quantity.product.title} - {self.product_quantity.quantity}"
