from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    count = models.IntegerField(default=1)
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} {self.price} "
