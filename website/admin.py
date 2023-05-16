from django.contrib import admin
from .models import School, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(School)
class SchoolAdmin(SummernoteModelAdmin):
    """
    Class for admins to filter and search for schools within the database
    """
    list_display = ('name', 'slug', 'region', 'gender_type', 'status')
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('region', 'gender_type', 'status')
    summernote_fields = ('description',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Class for admins to search Reviews within the database
    """
    list_display = ('name', 'body', 'school', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
