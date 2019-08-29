from django.shortcuts import render
from firstWEB.models import cal
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

def CalPage(request):
    return render(request,'cal.html')

def Cal(request):
    if request.POST:
        value_a = request.POST['valueA']
        value_b = request.POST['valueB']
        result = int(value_a) + int(value_b)
        cal.objects.create(value_a=value_a,value_b=value_b,result=result)
        return render(request,'result.html',context={'data':result})
    else:
        return HttpResponse('please visit us with POST')

def CalList(request):
    data = cal.objects.all()
    return render(request,'list.html',context={'data':data})

def DelData(request):
    cal.objects.all().delete()
    return HttpResponse('data Deleted')