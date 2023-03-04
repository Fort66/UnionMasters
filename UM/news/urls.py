from django.urls import path
from . import views
#from . models import News


urlpatterns = [
    path('', views.news_home, name='news_home'),
    #path('addnews/', views.news_home, name='news_home'),
]
