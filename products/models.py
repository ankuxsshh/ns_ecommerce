from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


TYPE = (
    ("Cashew","Cashew"),
    ("Almond","Almond"),
    ("Pista","Pista"),
    ("Dates","Dates"),
    ("Assorted","Assorted"),
    ("Combo","Combo")
)
AVAILABILITY = (
    ("In Stock", "In Stock"),
    ("Out of stock", "Out of stock")
)
class Products(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100, choices = TYPE, null=True)
    title = models.CharField(max_length=150, null=True)
    price = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    stock = models.BooleanField(null=True, default=True)
    qty = models.CharField(max_length=5, null=True)
    qcheck = models.CharField(max_length=5, null=True)
    shortD = models.TextField(null=True)
    discription = RichTextField(null=True)
    specification = RichTextField(null=True)
    img1 = models.ImageField(upload_to='Products/')
    img2 = models.ImageField(upload_to='Products/')
    img3 = models.ImageField(upload_to='Products/', blank=True)
    img4 = models.ImageField(upload_to='Products/', blank=True)
    
    def __str__(self):
        return self.title