from django.db import models

class Adress(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Students(models.Model):
    image = models.ImageField(upload_to='media/students/')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=18)
    address = models.ForeignKey(Adress, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
