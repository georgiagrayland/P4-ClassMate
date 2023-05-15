from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

region_options = (
    ("London & SE"),
    ("Manchester & NE"),
    ("Bristol & SW"),
    ("Newcastle & NE"),
)

status_options = (
    ("Fee-paying"),
    ("State Grammar"),
    ("Academy"),
)

gender_options = (
    ("Co-educational"),
    ("Girls"),
    ("Boys"),
)


# Create your models here.
class School(models.Model):
    """
    School model, which stores all information about the schools
    to be displayed on various pages of the website
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, unique=True)
    slug = models.SlugField(max_length=500, unique=True)
    region = models.CharField(max_length=200, choices=region_options)
    status = models.CharField(max_length=200, choices=status_options)
    gender_type = models.CharField(max_length=200, choices=gender_options)
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
