# Generated by Django 3.2.5 on 2021-07-09 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('wagtailsearchpromotions', '0002_capitalizeverbose'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('core', '0043_auto_20210412_1646'),
        ('ai_lab', '0039_ailabpublication'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AiLabPublication',
        ),
    ]
