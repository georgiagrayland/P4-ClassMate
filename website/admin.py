from django.contrib import admin
from .models import School
from django_summernote.admin import SummernoteModelAdmin


@admin.register(School)
class SchoolAdmin(SummernoteModelAdmin):
    """
    Class to show summernote UI to admins when working with the database
    """
    summernote_fields = ('description')
