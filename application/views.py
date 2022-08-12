from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from application.models import Task
# Create your views here.

def home(request):
    if request.method == 'POST':
        Name=request.POST.get('name')
        Age=request.POST.get('age')
        Time=request.POST.get('time')
        Desc=request.POST.get('description')
        task=Task(Name=Name,Age=Age,Time=Time,Desc=Desc)
        task.save()


    return render(request, 'home.html')

def task(request):
    tasks=Task.objects.all()
    new_var = {'alltask':tasks}
    return render(request,'task.html',new_var)

def update(request,id):
    tas=Task.objects.get(id=id)
    new_var = {'task':tas}
    if request.method == 'POST':
        Name=request.POST.get('name')
        Age=request.POST.get('age')
        Time=request.POST.get('time')
        Desc=request.POST.get('description')
        tas=Task(Name=Name,Age=Age,Time=Time,Desc=Desc)
        tas.save()
        return redirect('home')
    return render(request,'update.html',new_var)


def delete(request,id):
    tas=Task.objects.get(id=id)
    tas.delete()
    return redirect('home')




