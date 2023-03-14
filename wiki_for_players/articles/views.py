from django.shortcuts import render
from .models import Articles


def articles_home(request):
    articles = Articles.objects.all()
    return render(request, 'articles/articles_home.html', {'articles': articles})

