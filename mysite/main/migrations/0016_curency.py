# Generated by Django 4.1.7 on 2023-04-28 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_items_name_en_items_name_hy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='usd', max_length=20, verbose_name='Curency name')),
                ('kurs_amd', models.PositiveIntegerField(verbose_name='AMD kurs')),
            ],
            options={
                'verbose_name': 'Curency',
                'verbose_name_plural': 'Curency',
            },
        ),
    ]
