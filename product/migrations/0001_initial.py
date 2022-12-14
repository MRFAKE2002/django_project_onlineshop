# Generated by Django 4.0.2 on 2022-11-30 08:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('text', models.TextField()),
                ('price', models.PositiveIntegerField(default=0)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('datetime_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Create')),
                ('datetime_modified', models.DateTimeField(auto_now=True, verbose_name='Modified')),
            ],
        ),
    ]
