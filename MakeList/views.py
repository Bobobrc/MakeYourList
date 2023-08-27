from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import List, Task
from .forms import ListForm
from django.contrib import messages

# Create your views here.
def MainPage(request):
  if request.method=='POST':
    if request.POST['Submit'] == 'create_list':
      create_form = ListForm(request.POST)
      if create_form.is_valid():
        list_name = create_form.cleaned_data['list_name']
        list_password = create_form.cleaned_data['list_password']
        new_list = List(list_name = list_name, list_password = list_password)
        new_list.save()
        return redirect('ListPage', list_name = list_name)
    else:
      list_name = request.POST.get('list_name')
      try:
        existing_list = List.objects.get(list_name = list_name)
        return redirect('ListPage', list_name = list_name)
      except:
        raise Http404("List does not exist!")
  return render(request, 'makelist/firstpage.html')

def ListPage(request, list_name):
  the_list = List.objects.get(list_name=list_name)
  error_message = None
  if request.method == "POST":
    task_name = request.POST.get("task_name")
    list_password = request.POST.get("list_password")
    important = request.POST.get('important_task', False)
    if list_password == the_list.list_password:
      new_task = Task(list=the_list, task_name=task_name, important=important)
      new_task.save()
      return redirect('ListPage', list_name=list_name)
    else:
      error_message = "Wrong password. Please try again."
  tasks = Task.objects.filter(list=the_list)
  return render(request, 'makelist/list.html', {'list_name': list_name, 'tasks':tasks, 'error_message': error_message})