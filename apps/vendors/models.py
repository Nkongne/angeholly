from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vendor(models.Model):
    nom=models.CharField(max_length=255)
    cree_le=models.DateTimeField(auto_now_add=True)
    cree_par=models.OneToOneField(User,related_name='vendor',on_delete=models.CASCADE)

    class Meta:
        ordering=['nom']
    def __str__(self):
        return self.nom
    def get_balance(self):
        items=self.items.filter(vendor_paid=False,order__vendors__in=[self.id])
        return sum((item.product.price * item.quantity) for item in items)

    def get_paid_amount(self):
        items = self.items.filter(vendor_paid=True, order__vendors__in=[self.id])
        return sum((item.product.price * item.quantity) for item in items)