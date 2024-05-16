from django.db import models


# Create your models here.
class Student(models.Model):
    full_name = models.CharField(max_length=35)
    image = models.ImageField(upload_to='student/', blank=True, null=True)
    review = models.TextField(max_length=100)

    def __str__(self):
        return self.full_name
