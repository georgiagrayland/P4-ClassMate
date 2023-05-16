from django.shortcuts import render
from django.urls import path


def index(request):
    """
    View to return the index/homepage including desired content to be desired
    """

    return render(request, 'home/index.html', context)
