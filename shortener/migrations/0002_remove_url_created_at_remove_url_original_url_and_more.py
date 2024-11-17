# Generated by Django 5.1.3 on 2024-11-16 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='url',
            name='original_url',
        ),
        migrations.RemoveField(
            model_name='url',
            name='short_url',
        ),
        migrations.AddField(
            model_name='url',
            name='original',
            field=models.URLField(default='http://example.com'),
        ),
        migrations.AddField(
            model_name='url',
            name='shortened',
            field=models.CharField(default='placeholder', max_length=6, unique=True),
        ),
    ]
