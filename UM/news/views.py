from django.shortcuts import render
from .models import News

def news_home(request):
    news = News.objects.all()[:10]
    
    return render(request, 'news/news_home.html', {'news': news})
