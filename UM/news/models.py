from django.db import models
from django.urls import reverse_lazy
from django.db.models import ImageField, ForeignKey

class News(models.Model):
    NewsTitle = models.CharField(max_length=100, null=False, verbose_name='Заголовок')
    NewsAnonce = models.CharField(max_length=100, null=False, verbose_name='Анонс')
    NewsBody = models.TextField(verbose_name='Текст новости')
    NewsDatePosted = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    NewsPhoto = models.ImageField(upload_to='static/image/%Y/%m/%d', blank=True, null=True, verbose_name='Фото')

    def get_absolute_url(self):
        return reverse_lazy('news', kwargs = {'news_id': self.pk})   #f'/news/{self.id}' 
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-NewsDatePosted']

    
    
    def __str__(self):
        return f'{self.NewsTitle}'

