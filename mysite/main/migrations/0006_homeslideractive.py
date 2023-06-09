# Generated by Django 4.1.7 on 2023-04-02 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_headerinfo_account_en_headerinfo_account_hy_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeSliderActive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=30, verbose_name='SliderActive name1')),
                ('name1_hy', models.CharField(max_length=30, null=True, verbose_name='SliderActive name1')),
                ('name1_en', models.CharField(max_length=30, null=True, verbose_name='SliderActive name1')),
                ('name2', models.CharField(max_length=30, verbose_name='SliderActive name2')),
                ('name2_hy', models.CharField(max_length=30, null=True, verbose_name='SliderActive name2')),
                ('name2_en', models.CharField(max_length=30, null=True, verbose_name='SliderActive name2')),
                ('text', models.TextField(verbose_name='SliderActive text')),
                ('text_hy', models.TextField(null=True, verbose_name='SliderActive text')),
                ('text_en', models.TextField(null=True, verbose_name='SliderActive text')),
                ('button_name', models.CharField(max_length=20, verbose_name='SliderActive button name')),
                ('button_name_hy', models.CharField(max_length=20, null=True, verbose_name='SliderActive button name')),
                ('button_name_en', models.CharField(max_length=20, null=True, verbose_name='SliderActive button name')),
                ('img1', models.ImageField(upload_to='media', verbose_name='SliderActive image1')),
                ('img2', models.ImageField(upload_to='media', verbose_name='SliderActive image2')),
            ],
            options={
                'verbose_name': 'HomeSliderActive',
                'verbose_name_plural': 'HomeSliderActive',
            },
        ),
    ]
