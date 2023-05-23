from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views import View
from django.http import HttpResponse
from .models import School


class Home(generic.TemplateView):
    model = School
    template_name = 'index.html'


# Put in filerting tool if time
def schools_list(request):
    """
    A view that displays all schools for users to browse
    """
    schools = School.objects.all()
    total_number_of_schools = schools.count()

    context = {
        'schools': schools,
        'total_number_of_schools': total_number_of_schools,
    }

    return render(request, 'templates/schools.html', context)


class SchoolDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = School.objects
        school = get_object_or_404(queryset, slug=slug)
        comments = School.comments.filter(approved=True).order_by('created_on')
        rated = False
        if school.rating.filter(id=self.request.user.id).exists():
            rated = True

        return render(request, 'school_detail.html')
