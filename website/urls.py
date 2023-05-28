from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('schools/', views.schools_list, name='schools'),
    path(
        'schools/<slug:slug>/',
        views.SchoolDetail.as_view(), name='school_detail'),
    path('comments/', views.my_comments, name='my_comments'),
    path(
        'comments/edit/<int:comment_id>/',
        views.edit_comment, name='edit_comment'),
    path(
        'comments/delete/<int:comment_id>/',
        views.delete_comment, name='delete_comment'),
]
