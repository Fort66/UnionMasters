from django.urls import path
from . import views
#from . models import News


urlpatterns = [
    path('', views.NewsList.as_view(), name='news'),
    path('addnews/', views.NewsCreate.as_view(), name='addnews'),
    path('<int:pk>/', views.NewsDetail.as_view(), name='news_detail'),
    path('<int:pk>/update/', views.NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', views.NewsDelete.as_view(), name='news_delete'),
]
