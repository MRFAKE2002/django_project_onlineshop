# Generated by Django 4.0.2 on 2022-12-08 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='star',
            field=models.CharField(choices=[('1', 'bad'), ('1', 'normal'), ('1', 'good')], default=1, max_length=5, verbose_name='Star'),
            preserve_default=False,
        ),
    ]
