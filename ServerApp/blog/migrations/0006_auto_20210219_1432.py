# Generated by Django 3.1.3 on 2021-02-19 14:32

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210219_1339'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='articles',
            name='blog_articl_content_77405c_gin',
        ),
        migrations.AddField(
            model_name='articles',
            name='content_vector',
            field=django.contrib.postgres.search.SearchVectorField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articles',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddIndex(
            model_name='articles',
            index=django.contrib.postgres.indexes.GinIndex(fields=['content_vector'], name='blog_articl_content_5419e4_gin'),
        ),
    ]
