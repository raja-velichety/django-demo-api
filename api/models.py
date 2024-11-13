from django.db import models

from django.db import models
from decimal import Decimal

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=60, unique=True, blank=False)
    customer_name = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.customer_name}"


class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='details', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    line_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.line_total = Decimal(self.quantity) * self.price if self.quantity and self.price else Decimal('0.00')
        super().save(*args, **kwargs)

    def clean(self):
        if self.quantity <= 0:
            raise ValidationError("Quantity must be greater than zero.")
        if self.price <= 0:
            raise ValidationError("Price must be greater than zero.")

    def __str__(self):
        return f"Item: {self.description} (Qty: {self.quantity}, Price: {self.price}, Total: {self.line_total})"