from django.shortcuts import render

# Create your views here.
def MainPage(request):
  return render(request, 'makelist/firstpage.html')

def ListPage(request, list_name):
  return render(request, 'makelist/list.html')