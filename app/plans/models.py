from django.db import models
from recipes.models import ReceiptComponent


class DayPlan(models.Model):
    breakfast = models.ForeignKey(ReceiptComponent, on_delete=models.CASCADE, default=None)
    lunch = models.ForeignKey(ReceiptComponent, on_delete=models.CASCADE, default=None)
    dinner = models.ForeignKey(ReceiptComponent, on_delete=models.CASCADE, default=None)

    #
    # def __str__(self):
    #     return self.name
