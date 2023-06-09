from django.shortcuts import render, redirect,get_object_or_404
from .models import Task
from .forms import TaskForm

# Create your views here.
def task_list(request):
    tasks=Task.objects.all()
    return render(request,'task_list.html',{'tasks':tasks})

def task_detail(request,pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})

def task_create(request):
    if request.method== 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.save()
            return redirect('task_form.html',{'form':form})
    else:
        form=TaskForm()
    return render(request,'task_form.html',{'form':form})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')