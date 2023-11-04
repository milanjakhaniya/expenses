from django.db import models

class ExcelData(models.Model):
    date = models.DateField()
    time = models.TimeField()
    shop_code = models.IntegerField()
    product_id = models.IntegerField()
    product_type = models.IntegerField()
    weight = models.DecimalField(max_digits=25, decimal_places=2)
    quantity = models.DecimalField(max_digits=25, decimal_places=2)
    daily_rate = models.DecimalField(max_digits=25, decimal_places=2)
    rate = models.DecimalField(max_digits=25, decimal_places=2)
    amount = models.DecimalField(max_digits=25, decimal_places=2)
    opening_balance = models.DecimalField(max_digits=25, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=25, decimal_places=2)
    closing_balance = models.DecimalField(max_digits=25, decimal_places=2)

    def __str__(self):
        return f"Entry {self.pk}: {self.date}"



