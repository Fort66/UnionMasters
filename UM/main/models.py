from django.db import models
from django.db.models import ImageField, ForeignKey


class Cities(models.Model):
    CityName = models.CharField(max_length=100, blank=True, null=True, verbose_name='Название города')
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['CityName']

    def __str__(self):
        return self.CityName


class Users(models.Model):
    UserFirstName = models.CharField(max_length=100, null=False, verbose_name='Имя')
    UserLastName = models.CharField(max_length=100, blank=True, null=True, verbose_name='Фамилия')
    UserPhone = models.CharField(max_length=100, null=False, verbose_name='Телефон')
    UserAddress = models.CharField(max_length=200, null=False, verbose_name='Адрес')
    #UserApartment = models.CharField(max_length=100, blank=True, null=True)
    UserIntercomCode = models.CharField(max_length=100, blank=True, null=True, verbose_name='Код домофона')
    UserEmail = models.CharField(max_length=100, blank=True, null=True, verbose_name='Электронная почта')
    UserCityId = models.ForeignKey(Cities, on_delete=models.CASCADE, verbose_name='Ссылка на город')
    #UserStreetsId = models.ForeignKey('Streets', on_delete=models.CASCADE)
    # UserCitiesId = models.IntegerField()
    # UserStreetsId = models.IntegerField()
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['UserCityId']

    def __str__(self):
        return self.UserFirstName


class Technics(models.Model):
    TechnicName = models.CharField(max_length=100, null=False, verbose_name='Наименование техники')
    class Meta:
        verbose_name = 'Техника'
        verbose_name_plural = 'Техника'
        ordering = ['id']

    def __str__(self):
        return self.TechnicName


class Orders(models.Model):
    OrderDescriptions = models.CharField(max_length=100, blank=True, null=True, verbose_name='Описание поломки')
    OrderDate = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    UserId = ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Ссылка на пользователя')
    OrderTechnicsId = ForeignKey(Technics, on_delete=models.CASCADE, verbose_name='Ссылка на технику')
    # UserId = models.IntegerField()
    # OrderTechnicsId = models.IntegerField()
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-OrderDate']

    


#class Streets(models.Model):
    #StreetName = models.CharField(max_length=100, blank=True, null=True)
    #StreetCitiesId = ForeignKey(Cities, on_delete=models.CASCADE)
    # StreetCitiesId = models.IntegerField()


class LinksTable(models.Model):
    TelegramIcon = models.ImageField(upload_to='TelegramIcon', blank=True, null=True, verbose_name='Иконка Telegram')
    TelegramLink = models.CharField(max_length=100, blank=True, null=True, verbose_name='Ссылка на Telegram')
    WhatsappIcon = models.ImageField(upload_to='WhatsappIcon', blank=True, null=True, verbose_name='Иконка Whatsapp')
    WhatsappLink = models.CharField(max_length=100, blank=True, null=True, verbose_name='Ссылка на Whatsapp')
    VKIcon = ImageField(upload_to='VKIcon', blank=True, null=True, verbose_name='Иконка VK')
    VKLink = models.CharField(max_length=100, blank=True, null=True, verbose_name='Ссылка на VK')
    ViberIcon = models.ImageField(upload_to='ViberIcon', blank=True, null=True, verbose_name='Иконка Viber')
    ViberLink = models.CharField(max_length=100, blank=True, null=True, verbose_name='Ссылка на Viber')
    TwoGisIcon = models.ImageField(upload_to='TwoGisIcon', blank=True, null=True, verbose_name='Иконка 2Gis')
    TwoGisLink = models.CharField(max_length=100, blank=True, null=True, verbose_name='Ссылка на 2Gis')
    class Meta:
        verbose_name = 'Ссылка на соцсети'
        verbose_name_plural = 'Ссылки на соцсети'
        ordering = ['id']


# class Contacts(models.Model):
#     ContactCitiesId = ForeignKey(Cities, on_delete=models.CASCADE)
#     # ContactCitiesId = models.IntegerField()
#     ContactEmail = models.CharField(max_length=100, null=False)
#     ContactLegalAddress = models.CharField(max_length=100, null=False)


class Owner(models.Model):
    OwnerFirstName = models.CharField(max_length=100, null=False, verbose_name='Имя')
    OwnerLastName = models.CharField(max_length=100, null=False, verbose_name='Фамилия')
    OwnerPhone = models.CharField(max_length=100, null=False, verbose_name='Телефон')
    OwnerEmail = models.CharField(max_length=100, blank=True, null=True, verbose_name='Электронная почта')
    OwnerLegalAddress = models.CharField(max_length=100, blank=True, null=True, verbose_name='Адрес')
    OwnerCityId = ForeignKey(Cities, on_delete=models.CASCADE, verbose_name='Ссылка на город')
    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'
        ordering = ['id']

class MainIndexMedia(models.Model):
    photo = models.ImageField(upload_to='MainPageMedia', blank=True, null=True, verbose_name='Фото')
    class Meta:
        verbose_name = 'Услуги Фото'
        verbose_name_plural = 'Услуги Фото'

class MainIndexChapterOne(models.Model):
    title = models.TextField(verbose_name='Заголовок')
    class Meta:
        verbose_name = 'Услуги левая колонка'
        verbose_name_plural = 'Услуги левая колонка'
        ordering = ['id']

class MainIndexChapterTwo(models.Model):
    title = models.TextField(verbose_name='Заголовок')
    class Meta:
        verbose_name = 'Услуги правая колонка'
        verbose_name_plural = 'Услуги правая колонка'
        ordering = ['id']
        
class MainIndexAdditionService(models.Model):
    title = models.TextField(verbose_name='Заголовок')
    class Meta:
        verbose_name = 'Услуги доп услуги'
        verbose_name_plural = 'Услуги доп услуги'
        ordering = ['id']
        
class AboutUs(models.Model):
    descriptions = models.TextField(verbose_name='Описание')
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
        ordering = ['id']

class LogoSite(models.Model):
    logo = models.ImageField(upload_to='LogoSite', blank=True, null=True, verbose_name='Логотип')
    favicon = models.ImageField(upload_to='favicon', blank=True, null=True, verbose_name='Иконка')
    class Meta:
        verbose_name = 'Логотип'
        verbose_name_plural = 'Логотипы'
        ordering = ['id']

class UsersReviews(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Пользователь')
    review = models.TextField(verbose_name='Отзыв')
    ReviewDate = models.DateTimeField(auto_now_add=True, verbose_name='Дата отзыва')
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['id']