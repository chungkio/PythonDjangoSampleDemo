# Generated by Django 4.1.6 on 2023-03-13 02:32

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]