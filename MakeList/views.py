from django.shortcuts import render, redirect
from django.http import Http404
from .models import List
from .forms import ListForm

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
  return render(request, 'makelist/list.html')