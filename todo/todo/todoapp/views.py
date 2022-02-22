from django.shortcuts import render, redirect
from .forms import taskupdate

# Create your views here.
from todoapp.models import task


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        sv = task(name=name, priority=priority, date=date)
        sv.save()
    obj = task.objects.all()

    return render(request, "home.html", {"obj": obj})


def delete(request, taskid):
    dl = task.objects.get(id=taskid)
    if request.method == 'POST':
        dl.delete()
        return redirect('/')
    return render(request, "delete.html")


def update(request, taskid):
    tk = task.objects.get(id=taskid)
    f = taskupdate(request.POST or None, instance=tk)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, "update.html",{'tk':tk,'f':f})