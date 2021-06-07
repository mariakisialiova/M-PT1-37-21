# Generated by Django 3.2.3 on 2021-05-25 12:29

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=240, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pinned', models.BooleanField(default=False, verbose_name='Pinned')),
                ('title', models.CharField(max_length=400, verbose_name='Title')),
                ('description', tinymce.models.HTMLField(blank=True, verbose_name='Description')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('color', models.CharField(choices=[('a', 'yellow'), ('b', 'white'), ('c', 'green'), ('d', 'red'), ('e', 'blue')], default='a', max_length=1, verbose_name='Color')),
                ('tag', models.ManyToManyField(blank=True, to='notebook.Tags')),
            ],
            options={
                'ordering': ['-pinned', '-timestamp'],
            },
        ),
    ]