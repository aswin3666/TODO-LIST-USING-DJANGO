from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm
# Create your views here.
def index(request):
    form=TodoForm()
    return render(request,'index.html',{'form':form,})
def submit(request):
    form=TodoForm()
    todos=Todo.objects.all()
    if request.method=='POST':
        form=TodoForm(request.POST or None)
        if form.is_valid():
            form.save()
    return render(request,'index.html',{'form':form,'todos':todos})
def update(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    form=TodoForm(instance=todo)
    if request.method=='POST':
        form=TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('submit')
    return render(request,'update.html',{'form':form,'todo':todo})
def delete(request,todo_id):
    if request.method=='POST':
        Todo.objects.get(id=todo_id).delete()
        return redirect('submit')

