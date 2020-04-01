# Generated by Django 3.0.4 on 2020-04-01 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('core', '0002_auto_20200401_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionpage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sectionpage_hero_image', to='images.NHSXImage'),
        ),
    ]
