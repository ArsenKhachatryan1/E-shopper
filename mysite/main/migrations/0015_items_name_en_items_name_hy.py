# Generated by Django 4.1.7 on 2023-04-18 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='name_en',
            field=models.CharField(max_length=60, null=True, verbose_name='Item name'),
        ),
        migrations.AddField(
            model_name='items',
            name='name_hy',
            field=models.CharField(max_length=60, null=True, verbose_name='Item name'),
        ),
    ]