# Generated by Django 4.1.7 on 2023-03-04 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_remove_news_newsauthor"),
    ]

    operations = [
        migrations.DeleteModel(
            name="News",
        ),
    ]
