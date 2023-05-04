from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, View, FormView, RedirectView
#from .models import MainIndexChapterOne, MainIndexChapterTwo

# class IndexList(ListView):
#     model = MainIndexChapterOne, MainIndexChapterTwo
#     template_name = 'index.html'
#     context_object_name = 'index'
#     extra_context = {'title': 'Главная страница'}

def get_context_data(self, *, object_list = None,**kwargs):
    context = super().get_context_data(**kwargs)
    context['title'] = 'Главная страница'
    return context

    def get_queryset(self):
        return News.objects.all()


def index(request):
    data = {
        'title': 'Главная страница',
        
    }
    return render(request, 'main/index.html', data)

def about(request):
    data = {
        'title': 'О нас',
        
    }
    return render(request, 'main/about.html', data)

def contacts(request):
    data = {
        'title': 'Контакты',
        
    }
    return render(request, 'main/contacts.html', data)