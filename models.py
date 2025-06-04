from django.db import models

class MangoExport(models.Model):
    class Meta:
        app_label = 'mango_export'
    CATEGORY_CHOICES = [
        ('LANGRA', 'Langra'),
        ('FOZLI', 'Fozli'),
        ('AMROPLOI', 'Amroploi'),
        ('HIM_SHAGAR', 'Him Shagar'),
        ('HARIVANGA', 'HariVanga'),
        ('GOPALVOG', 'Gopalvog'),
        ('BANANA_MANGO', 'Banana Mango'),
        ('KHIRSHAPATI', 'KhirshaPati'),
    ]

    order_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, help_text='Quantity in Kg')
    total_price = models.DecimalField(max_digits=12, decimal_places=2, editable=False)
    availability = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.total_price = self.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.category} - Order {self.order_id}"