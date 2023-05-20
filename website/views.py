from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views import View
from .models import School


class Home(generic.TemplateView):
    model = School
    template_name = 'index.html'


class SchoolsList(generic.ListView):
    model = School
    # queryset = School.objects.order_by('percentage_gcse_5_above')
    template_name = 'schools.html'


class SchoolDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = School.objects
        school = get_object_or_404(queryset, slug=slug)
        comments = School.comments.filter(approved=True).order_by('created_on')
        rated = False
        if school.rating.filter(id=self.request.user.id).exists():
            rated = True

        return render(request, 'school_detail.html')
