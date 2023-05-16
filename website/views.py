from django.shortcuts import render
from django.views import generic
from .models import School


class SchoolsList(generic.ListView):
    model = School
    queryset = School.objects.filter(name).order_by('percentage_gcse_5_above')
    template_name = 'schools.html'
