from django.contrib import admin
from webapp.models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ['pk', 'description', 'status', 'full_description', 'date_of_completion']
    list_filter = ['date_of_completion']
    list_display_links = ['pk', 'description']
    search_fields = ['description', 'status']
    fields = ['description', 'status', 'full_description', 'date_of_completion']


admin.site.register(Task, TaskAdmin)
