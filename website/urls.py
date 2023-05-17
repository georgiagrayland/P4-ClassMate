from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    # path('schools_list', views.SchoolsList().as_view, name='schools'),
    path('<slug:slug>/', views.SchoolDetail.as_view(), name='school_detail'),
]
