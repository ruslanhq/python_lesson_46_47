# Generated by Django 2.2 on 2019-09-09 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_task_full_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_of_completion',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Дата выполнения'),
        ),
    ]