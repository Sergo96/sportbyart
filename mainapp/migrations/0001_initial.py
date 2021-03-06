# Generated by Django 3.1.7 on 2021-03-06 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Title')),
                ('image', models.ImageField(upload_to='article', verbose_name='Image')),
                ('short_desc', models.CharField(max_length=200, verbose_name='Short description')),
                ('content', models.TextField(verbose_name='Content')),
                ('publication', models.DateTimeField(auto_now_add=True, verbose_name='Publication')),
                ('ratings', models.PositiveIntegerField(default=0, verbose_name='ratings')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20, verbose_name='user name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('comment_content', models.TextField(verbose_name='Comment content')),
                ('publication_date', models.DateTimeField(auto_now_add=True, verbose_name='publication date')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.article')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
