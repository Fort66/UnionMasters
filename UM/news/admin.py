from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','NewsTitle','NewsBody','NewsDatePosted')
    list_display_links = ('id','NewsTitle','NewsBody','NewsDatePosted')
    #search_fields = ('id','BlogsTitle','BlogsBody','BlogsDatePosted','BlogsAuthor')
    list_filter = ('id','NewsTitle','NewsBody','NewsDatePosted')
    #list_editable = ('BlogsAuthor')