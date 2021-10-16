from django.db import models


class DeliveryPlan(models.Model):
    PLAN_DATE = models.CharField(max_length=15)
    DP_MNYR = models.CharField(max_length=6)
    SBU_ID = models.CharField(max_length=10)
    SALES_AREA_ID = models.CharField(max_length=10)
    SORT_ORDER = models.CharField(max_length=10, null=True)
    STATUS = models.CharField(max_length=10)
    CREATED_BY = models.CharField(max_length=10)
    CREATED_AT = models.CharField(max_length=30)
    UPDATED_BY = models.CharField(max_length=10, null=True)
    UPDATED_AT = models.CharField(max_length=30)

    def __str__(self):
        return self.PLAN_DATE
