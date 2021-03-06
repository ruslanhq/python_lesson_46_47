# Generated by Django 2.2 on 2019-09-09 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20190909_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_of_completion',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Дата выполнения'),
        ),
        migrations.AlterField(
            model_name='task',
            name='full_description',
            field=models.TextField(blank=True, default=None, max_length=500, null=True, verbose_name='Подробное описание'),
        ),
    ]
