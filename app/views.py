from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('topic is inserted')
    
    return render(request,'topic.html')

def webpage(request):
    if request.method=='POST':
        t=request.POST['t']
        n=request.POST['n']
        u=request.POST['u']
        e=request.POST['e']

        TO=Topic.objects.get_or_create(topic_name=t)[0]
        TO.save()
        WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
        WO.save()

        return HttpResponse("webpage is inserted")
    return render(request,'webpage.html')


def records(request):
    if request.method=='POST':
        n=request.POST['n']
        a=request.POST['a']
        d=request.POST['d']
        WO=Webpage.objects.get_or_create(name=n)[0]
        WO.save() 
        RO=Records.objects.get_or_create(name=WO,author=a,date=d)[0]
        RO.save()

        return HttpResponse('records is inserted')
    return render(request,'records.html')