from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','NewsTitle','NewsAnonce', 'NewsBody','NewsDatePosted', 'NewsPhoto')
    list_display_links = ('id','NewsTitle', 'NewsAnonce', 'NewsBody','NewsDatePosted', 'NewsPhoto')
    #search_fields = ('id','BlogsTitle','BlogsBody','BlogsDatePosted','BlogsAuthor')
    list_filter = ('id','NewsTitle', 'NewsAnonce', 'NewsBody','NewsDatePosted')
    #list_editable = ('BlogsAuthor')