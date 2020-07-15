# Generated by Django 3.0.4 on 2020-04-08 13:13

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ("taggit", "0003_taggeditem_add_unique_index"),
        ("blog_posts", "0010_blogpost_canonical_rel"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogTags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "content_object",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="blog_posts_blogtags_items",
                        to="blog_posts.BlogPost",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="blog_posts_blogtags_items",
                        to="taggit.Tag",
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
        migrations.DeleteModel(name="BlogTag",),
        migrations.AlterField(
            model_name="blogpost",
            name="tags",
            field=modelcluster.contrib.taggit.ClusterTaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="blog_posts.BlogTags",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
