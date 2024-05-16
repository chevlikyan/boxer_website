from django.db import models


# Create your models here.
class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Blog(models.Model):
    full_name = models.CharField(max_length=35)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    review = models.TextField(max_length=100)
    slug = models.SlugField()
    pub_date = models

    def __str__(self):
        return self.full_name
