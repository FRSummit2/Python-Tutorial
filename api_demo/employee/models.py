from django.db import models


class employees(models.Model):
    firstName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=15)
    empId = models.IntegerField()

    def __str__(self):
        return self.firstName
