# Generated by Django 3.2.8 on 2022-04-19 20:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import places.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=1000)),
                ('localization', models.CharField(default='', max_length=200)),
                ('title', models.CharField(default='', max_length=200)),
                ('street', models.CharField(blank=True, default='', max_length=200)),
                ('city', models.CharField(blank=True, default='', max_length=200)),
                ('post_code', models.CharField(blank=True, default='', max_length=200)),
                ('state', models.CharField(blank=True, default='', max_length=200)),
                ('country', models.CharField(blank=True, default='', max_length=200)),
                ('category', models.CharField(default='', max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(blank=True, null=True)),
                ('parent_com', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=places.models.upload_path)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.post')),
            ],
        ),
    ]
