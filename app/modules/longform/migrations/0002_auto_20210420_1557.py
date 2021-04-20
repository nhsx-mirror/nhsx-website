# Generated by Django 3.1.8 on 2021-04-20 15:57

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ("longform", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="longformpost",
            name="history",
            field=wagtail.core.fields.RichTextField(
                blank=True,
                verbose_name="Version history (leave blank for initial publication)",
            ),
        ),
        migrations.AddField(
            model_name="longformpost",
            name="updated_at",
            field=models.DateTimeField(
                blank=True,
                null=True,
                verbose_name="Updated at (leave blank for initial publication)",
            ),
        ),
    ]
