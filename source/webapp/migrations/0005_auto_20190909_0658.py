# Generated by Django 2.2 on 2019-09-09 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20190909_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_of_completion',
            field=models.DateField(default='', verbose_name='Дата выполнения'),
        ),
    ]
