# Generated by Django 5.1.3 on 2025-06-07 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelmodel',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Tavsif'),
        ),
        migrations.AddField(
            model_name='travelmodel',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Tavsif'),
        ),
        migrations.AddField(
            model_name='travelmodel',
            name='description_uz',
            field=models.TextField(blank=True, null=True, verbose_name='Tavsif'),
        ),
        migrations.AddField(
            model_name='travelmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='travel_image/', verbose_name='Rasm'),
        ),
        migrations.AddField(
            model_name='travelmodel',
            name='name_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='travelmodel',
            name='name_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nomi'),
        ),
        migrations.AddField(
            model_name='travelmodel',
            name='name_uz',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nomi'),
        ),
    ]
