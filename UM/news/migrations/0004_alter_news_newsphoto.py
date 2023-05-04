# Generated by Django 4.1.7 on 2023-03-12 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0003_news_newsanonce"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="NewsPhoto",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="static/image/%Y/%m/%d",
                verbose_name="Фото",
            ),
        ),
    ]