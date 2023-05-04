from django.shortcuts import render, redirect
from .forms import NewsForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, View, FormView, RedirectView
from .models import News
from .utils import MyMixin


class NewsList(ListView, MyMixin):
    model = News
    template_name = 'news/news_home.html'
    context_object_name = 'news'
    extra_context = {'title': 'Наши новости'}
    mixin_group = ''

    def get_context_data(self, *, object_list = None,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Наши новости'
        context['mixin_group'] = self.get_prop()
        return context

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

    def get_context_data(self, *, object_list = None,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = News.objects.get(pk=self.kwargs['pk'])
        return context

    def get_queryset(self):
        return News.objects.filter(news_id = self.kwargs['pk'])

class NewsUpdate(UpdateView):
    model = News
    template_name = 'news/addnews.html'
    context_object_name = 'news_update'
    form_class = NewsForm

    def get_context_data(self, *, object_list = None,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = News.objects.get(pk=self.kwargs['pk'])
        return context

    def get_queryset(self):
        return News.objects.filter(news_id = self.kwargs['pk'])

class NewsDelete(DeleteView):
    model = News
    template_name = 'news/news_delete.html'
    #context_object_name = 'news_delete'
    success_url = '/news/'
    
    def get_context_data(self, *, object_list = None,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = News.objects.get(pk=self.kwargs['pk'])
        return context

    def get_queryset(self):
        return News.objects.filter(news_id = self.kwargs['pk'])