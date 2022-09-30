from django.db import models
# database representation/defination
# Create your models here.
class Book(models.Model):
    book_code = models.CharField(max_length=50)
    book_name = models.CharField(max_length=150)
    author_name = models.CharField(max_length=150)
    date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f'BOOK: {self.book_name}'
