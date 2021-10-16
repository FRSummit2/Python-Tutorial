from django.db import models


class blogs(models.Model):
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=150)
    blogId = models.IntegerField()

    def __str__(self):
        return self.title
