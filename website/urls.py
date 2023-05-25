from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('schools/', views.schools_list, name='schools'),
    path('<slug:slug>/', views.SchoolDetail.as_view(), name='school_detail'),
    path('my_comments/', views.my_comments, name='my_comments'),
]
