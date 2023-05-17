from django.shortcuts import render
from django.views import generic
from django.views import View
from .models import School


def index(request):
    """
    Returns the Homepage
    """
    return render(request, 'index.html')


class SchoolsList(generic.ListView):
    model = School
    queryset = School.objects.order_by('percentage_gcse_5_above')
    template_name = 'schools.html'
