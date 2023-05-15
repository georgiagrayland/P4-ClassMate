from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, unique=True)
    slug = models.SlugField(max_length=500, unique=True)
    region = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    gender_type = models.CharField(max_length=200)
    class_size = models.IntegerField(max_length=3)
    avg_maths_grade = models.IntegerField(max_length=2)
    avg_english_grade = models.IntegerField(max_length=2)
    percentage_gcse_5 = models.IntegerField(max_length=10)
    featured_image = models.CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    specialisation = models.CharField()
    description = models.TextField()
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.title