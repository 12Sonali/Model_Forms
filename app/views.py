from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
from app.models import *
def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}

    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()

            QLTO=Topic.objects.all()
            d1={'QLTO':QLTO}
            return render(request,'display_topic.html',d1)
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}

    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()

            QLWO=WebPage.objects.all()
            d1={'QLWO':QLWO}
            return render(request,'display_Webpage.html',d1)
    return render(request,'insert_Webpage.html',d)


def insert_Accessrecord(request):
    EAFO=AccessrecordForm()
    d={'EAFO':EAFO}

    if request.method=='POST':
        AFDO=AccessrecordForm(request.POST)
        if AFDO.is_valid():
            AFDO.save()

            QLAO=AccessRecord.objects.all()
            d1={'QLAO':QLAO}
            return render(request,'display_accessrecord.html',d1)
    return render(request,'insert_accessrecord.html',d)
