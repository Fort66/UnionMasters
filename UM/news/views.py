from django.shortcuts import render, redirect
from .forms import NewsForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, View, FormView, RedirectView
from .models import News


class NewsList(ListView):
    model = News
    template_name = 'news/news_home.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.all()

class NewsCreate(CreateView):
    model = News
    template_name = 'news/addnews.html'
    form_class = NewsForm
    success_url = '/news/'
    
class NewsDetail(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news_detail'

class NewsUpdate(UpdateView):
    model = News
    template_name = 'news/addnews.html'
    #context_object_name = 'news_update'
    form_class = NewsForm

class NewsDelete(DeleteView):
    model = News
    template_name = 'news/news_delete.html'
    #context_object_name = 'news_delete'
    success_url = '/news/'
    
    