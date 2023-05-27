from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from cloudinary.models import CloudinaryField

region_options = (
    ("London", "London"),
    ("Manchester", "Manchester"),
    ("Bristol", "Bristol"),
    ("Newcastle", "Newcastle"),
)

status_options = (
    ("Fee-paying", "Fee-paying"),
    ("State Grammar", "State Grammar"),
    ("Academy", "Academy"),
)

gender_options = (
    ("Co-educational", "Co-educational"),
    ("Girls", "Girls"),
    ("Boys", "Boys"),
)


# Create your models here.
class School(models.Model):
    """
    School model, which stores all information about the schools
    to be displayed on various pages of the website
    """
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500, unique=True)
    slug = models.SlugField(max_length=500, unique=True)
    region = models.CharField(max_length=200, choices=region_options)
    status = models.CharField(max_length=200, choices=status_options)
    gender_type = models.CharField(max_length=200, choices=gender_options)
    class_size = models.IntegerField(validators=[MaxValueValidator(40)])
    avg_gcse_maths_grade = models.IntegerField()
    avg_gcse_english_grade = models.IntegerField()
    percentage_gcse_5_above = models.IntegerField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    specialisation = models.CharField(max_length=200)
    description = models.TextField()
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return self.name

    def school_location(self):
        return self.region


class Comment(models.Model):
    """
    Model for discussion section on each school page
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

        def __str__(self):
            return f"Comment {self.body} wrriten by {self.name}"
