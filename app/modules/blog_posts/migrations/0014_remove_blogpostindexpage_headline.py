# Generated by Django 3.0.4 on 2020-04-09 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog_posts", "0013_auto_20200409_1203"),
    ]

    operations = [
        migrations.RemoveField(model_name="blogpostindexpage", name="headline",),
    ]
