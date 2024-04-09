from django.db import models
from student.models import Students


class Author(models.Model):
    first_name = models.CharField(max_length=50,verbose_name="First Name")
    last_name = models.CharField(max_length=50,verbose_name="Last Name")
    birth_date = models.DateField(auto_now_add=True, verbose_name="Birth Date")

    def __str__(self):
        return f"{self.id} {self.first_name}  {self.last_name}"

class Comments(models.Model):
    text = models.TextField(verbose_name="Comments")
    student = models.ForeignKey(Students, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.text}"

class Book(models.Model):
    title = models.CharField(max_length=200,verbose_name="Book Title")
    description = models.TextField(verbose_name="Book Description")
    price = models.FloatField(verbose_name="Cost")
    comments = models.ManyToManyField(Comments,verbose_name="UsersComments")
    count = models.IntegerField(default=1)
    image = models.ImageField(upload_to="media/book/")
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f"{self.title} {self.price} "

class BookingBook(models.Model):
    student = models.ManyToManyField(Students,verbose_name="Students")
    book = models.ManyToManyField(Book,verbose_name="book")
    take_date = models.DateField(auto_now_add=True)
    return_date = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} {self.book}"

