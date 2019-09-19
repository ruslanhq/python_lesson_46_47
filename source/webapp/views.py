from django.shortcuts import render, get_object_or_404, redirect

from webapp.forms import TaskForm
from webapp.models import Task, STATUS_CHOICES

# Create your views here.


def index_view(request, *args, **kwargs):
    return render(request, 'index.html')


def task_list(request, *args, **kwargs):
    tasks = Task.objects.all()
    return render(request, 'list.html', context={
        'tasks': tasks
    })


def task_view(request, pk):
    tasks = get_object_or_404(Task, pk=pk)
    return render(request, 'task.html', context={
        'tasks': tasks
    })


def create_task(request, *args, **kwargs):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'add.html', context={
            'form': form,
            'status_choices': STATUS_CHOICES
        })
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            tasks = Task.objects.create(
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                date_of_completion=form.cleaned_data['date_of_completion'],
                full_description=form.cleaned_data['full_description']
            )
            return redirect('task_view', pk=tasks.pk)
        else:
            return render(request, 'add.html', context={
                'form': form
            })


def update_task(request, pk):
    tasks = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'update.html', context={
            'status_choices': STATUS_CHOICES,
            'tasks': tasks
        })
    elif request.method == 'POST':
        tasks.description = request.POST.get('description')
        tasks.status = request.POST.get('status')
        tasks.date_of_completion = request.POST.get('date_of_completion')
        tasks.full_description = request.POST.get('full_description')
        if tasks.date_of_completion == '':
            tasks.date_of_completion = None
        tasks.save()
        return redirect('task_view', pk=tasks.pk)


def delete_task(request, pk):
    tasks = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        return render(request, 'delete.html',{
            'tasks': tasks
        })
    elif request.method == "POST":
        tasks.delete()
        return redirect('index')

