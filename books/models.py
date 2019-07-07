from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=100)
    rate = models.IntegerField()
    quantity = models.IntegerField()

    @property
    def in_stock(self):
        return self.quantity > 0
