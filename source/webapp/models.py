from django.db import models

# Create your models here.

STATUS_CHOICES = (
    ('new', 'New'),
    ('in_progress', 'In Progress'),
    ('done', 'Done'),
)


class Task(models.Model):
    description = models.CharField(max_length=200, verbose_name='Описание', null=False, blank=False)
    status = models.CharField(max_length=20, verbose_name='Статус', default=STATUS_CHOICES[0][0],
                              choices=STATUS_CHOICES)
    date_of_completion = models.DateField(null=True, blank=True, verbose_name='Дата выполнения', default=None, )
    full_description = models.TextField(max_length=500, verbose_name='Подробное описание', default=None, blank=True, null=True)

    def __str__(self):
        return self.description


