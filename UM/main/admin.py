from django.contrib import admin
#from django.urls import path, include

from .models import MainIndexChapterOne, MainIndexChapterTwo, Users, Technics, Orders, Cities, Owner, AboutUs, UsersReviews
#MainPageChapterOne, MainPageChapterTwo, MainPageAdditionService,
# MainPageMedia, Users, Technics, Orders, Cities, LinksTable, Owner, Blogs, AboutUs

@admin.register(MainIndexChapterOne)
class MainIndexChapterOneAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')
    #search_fields = ('id','title')
    list_filter = ('id','title')

@admin.register(MainIndexChapterTwo)
class MainIndexChapterTwoAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')
    #search_fields = ('id','title')
    list_filter = ('id','title')

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id','UserFirstName','UserLastName','UserPhone','UserCityId','UserIntercomCode','UserEmail','UserAddress')
    list_display_links = ('id','UserFirstName','UserLastName','UserPhone','UserCityId','UserIntercomCode','UserEmail','UserAddress')
    #search_fields = ('id','UserFirstName','UserLastName','UserPhone','UserCityId','UserIntercomCode','UserEmail','UserAddress')
    list_filter = ('id','UserFirstName','UserLastName','UserPhone','UserCityId','UserIntercomCode','UserEmail','UserAddress')

@admin.register(Technics)
class TechnicsAdmin(admin.ModelAdmin):
    list_display = ('id','TechnicName')
    list_display_links = ('id','TechnicName')
    #search_fields = ('id','TechnicName')
    list_filter = ('id','TechnicName')

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id','OrderDescriptions','OrderDate','UserId','OrderTechnicsId')
    list_display_links = ('id','OrderDescriptions','OrderDate','UserId','OrderTechnicsId')
    #search_fields = ('id','OrderDescriptions','OrderDate','UserId','OrderTechnicsId')
    list_filter = ('id','OrderDescriptions','OrderDate','UserId','OrderTechnicsId')

@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    list_display = ('id','CityName')
    list_display_links = ('id','CityName')
    #search_fields = ('id','CityName')
    list_filter = ('id','CityName')
    #list_editable = ('CityName')

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('id','OwnerFirstName','OwnerLastName','OwnerPhone','OwnerLegalAddress','OwnerCityId','OwnerEmail')
    list_display_links = ('id','OwnerFirstName','OwnerLastName','OwnerPhone','OwnerLegalAddress','OwnerCityId','OwnerEmail')
    #search_fields = ('id','OwnerFirstName','OwnerLastName','OwnerPhone','OwnerLegalAddress','OwnerCityId','OwnerEmail')
    list_filter = ('id','OwnerFirstName','OwnerLastName','OwnerPhone','OwnerLegalAddress','OwnerCityId','OwnerEmail')

# @admin.register(News)
# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('id','NewsTitle','NewsBody','NewsDatePosted')
#     list_display_links = ('id','NewsTitle','NewsBody','NewsDatePosted')
#     #search_fields = ('id','BlogsTitle','BlogsBody','BlogsDatePosted','BlogsAuthor')
#     list_filter = ('id','NewsTitle','NewsBody','NewsDatePosted')
#     #list_editable = ('BlogsAuthor')

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id','descriptions')
    list_display_links = ('id','descriptions')
    #search_fields = ('id','descriptions')
    list_filter = ('id','descriptions')

@admin.register(UsersReviews)
class UsersReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'review', 'ReviewDate')
    list_display_links = ('id', 'user', 'review', 'ReviewDate')
    list_filter = ('id', 'user', 'review', 'ReviewDate')




