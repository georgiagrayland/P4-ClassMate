from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views import View
from django.http import HttpResponse
from .models import School
from .forms import CommentForm


class Home(generic.TemplateView):
    model = School
    template_name = 'index.html'


def schools_list(request):
    """
    A view that displays all schools for users to browse
    """
    schools = School.objects.all()
    total_number_of_schools = schools.count()

    context = {
        "schools": schools,
        "total_number_of_schools": total_number_of_schools,
    }

    return render(request, 'schools.html', context)


class SchoolDetail(View):

    def get(self, request, slug, *args, **kwargs):
        """
        View that shows each school on an individual page
        """
        queryset = School.objects.all()
        school = get_object_or_404(queryset, slug=slug)
        comments = school.comments.filter(approved=True).order_by(
            '-created_on')

        return render(
            request,
            "school_detail.html",
            {
                "school": school,
                "comments": comments,
                "commented": False,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = School.objects.all()
        school = get_object_or_404(queryset, slug=slug)
        comments = school.comments.filter(approved=True).order_by(
            '-created_on')

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.school = school
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "school_detail.html",
            {
                "school": school,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
            },
        )
