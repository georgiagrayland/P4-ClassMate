from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('schools/', views.schools_list, name='schools'),
    path('<slug:slug>/', views.school_detail, name='school_detail'),
]
