# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-10 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20160408_2339'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannedWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='bandwords',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='article_tag',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='age',
        ),
        migrations.AddField(
            model_name='article',
            name='article_tag',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
        migrations.AddField(
            model_name='article',
            name='comments_number',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(error_messages={'unique': 'This tag already exists.'}, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_image',
            field=models.ImageField(blank=True, upload_to='profile_images'),
        ),
        migrations.DeleteModel(
            name='BandWords',
        ),
    ]