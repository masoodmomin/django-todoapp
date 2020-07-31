from django.shortcuts import render
from django.http import HttpResponseRedirect
from todoapp.models import ToDo
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

# Create your views here.
def index(request):
    todos = ToDo.objects.all().order_by("-date")
    return render(request,'todoapp/index.html', {"todos": todos})

@csrf_exempt
def add_todo(request):
    content = request.POST["content"]
    if(content != ""):
        current_date = timezone.now()
        created_obj = ToDo.objects.create(date=current_date,text=content,is_completed=False)
    return HttpResponseRedirect("/todoapp")

def delete_todo(request, todo_id):
    ToDo.objects.get(pk=todo_id).delete()
    return HttpResponseRedirect("/todoapp")

def complete(request, todo_id):
    td = ToDo.objects.get(pk=todo_id)
    td.is_completed = not td.is_completed
    td.save()
    return HttpResponseRedirect("/todoapp")