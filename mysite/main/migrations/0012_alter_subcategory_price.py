# Generated by Django 4.1.7 on 2023-04-03 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_subcategory_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='SubCategory price'),
        ),
    ]
