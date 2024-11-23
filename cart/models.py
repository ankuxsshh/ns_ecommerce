from django.db import models

# Create your models here.
class Cart(models.Model):
    id= models.AutoField(primary_key=True)
    pid = models.IntegerField(null=True)
    add_user = models.CharField(max_length=200,null=True)
    item_title = models.CharField(max_length=250,null=True)
    qty = models.IntegerField(null=True)
    rate = models.IntegerField(null=True)
    sub_total = models.IntegerField(default=1)
    