# Generated by Django 4.0.2 on 2022-12-08 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_star'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='star',
            field=models.CharField(choices=[('1', 'very bad'), ('2', 'bad'), ('3', 'normal'), ('4', 'good'), ('5', 'perfect')], max_length=5, verbose_name='Star'),
        ),
        migrations.AlterField(
            model_name='product',
            name='star',
            field=models.CharField(choices=[('1', 'very bad'), ('2', 'bad'), ('3', 'normal'), ('4', 'good'), ('5', 'perfect')], max_length=5, verbose_name='Star'),
        ),
    ]
