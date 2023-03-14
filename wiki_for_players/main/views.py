from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from articles.models import Articles
from articles.forms import ArticlesForm
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import *


def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html', data)


class ArticlesDetailView(DetailView):
    model = Articles
    template_name = 'main/details_view.html'
    context_object_name = 'article'

class ArticlesUpdateView(UpdateView):
    model = Articles
    template_name = 'main/create.html'

    form_class = ArticlesForm

class ArticlesDeleteView(DeleteView):
    model = Articles
    success_url = '/hollow_knight_characters'
    template_name = 'main/article_delete.html'


def dead_cells(request):
    return render(request, 'main/dead_cells.html')


def hollow_knight(request):
    return render(request, 'main/hollow_knight.html')


def hollow_knight_characters(request):
    articles = Articles.objects.all()
    return render(request, 'main/hollow_knight_characters.html', {'articles': articles})

def create(request):
    error = ""
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('hollow_knight_characters')
        else:
            error = 'Форма была неверной'
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', data)



class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('login')








