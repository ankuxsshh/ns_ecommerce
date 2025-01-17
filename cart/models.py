from django.db import models

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    pid = models.IntegerField(null=True)
    add_user = models.CharField(max_length=200, null=True)
    item_title = models.CharField(max_length=250, null=True)
    qty = models.IntegerField(null=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # Updated
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Updated

    def __str__(self):
        return f"{self.item_title} ({self.qty})"
