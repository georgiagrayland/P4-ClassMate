from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views import View
from django.http import HttpResponse, HttpRequest
from .models import School, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


class Home(generic.TemplateView):
    """
    View that displays the homepage
    """
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


def my_comments(request):
    """
    View that displays all comments a user has made back to them
    """
    author = User.objects.get(username=request.user.username)
    comments = Comment.objects.filter(author=author)

    context = {
        "author": author,
        "comments": comments,
    }
    return render(request, 'my_comments.html', context)


def edit_comment(request, comment_id):
    """
    View that allows users to edit comments they have made
    """
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        comment.body = request.POST.get('comment_body')
        comment.save()
        return redirect('my_comments')

    return render(request, 'edit_comment.html', {'comment': comment})


def delete_comment(request, comment_id):
    """
    View that allows users to delete any comments they have made
    """
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        comment.delete()
        return redirect('my_comments')

    return render(request, 'delete_comment.html')


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
            comment.author = User.objects.get(username=request.user.username)
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
