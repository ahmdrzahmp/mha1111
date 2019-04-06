from django.shortcuts import render

from .models import Upload, Pages, Link, Message, Sponsor, Content, Workshop, Register, Language, Payment, Setting, \
    Articles


# Create your views here.

def index_url(request):
    index_url = Upload.objects.all()
    index_url = Pages.objects.all()
    index_url = Link.objects.all()
    index_url = Message.objects.all()
    index_url = Sponsor.objects.all()
    index_url = Content.objects.all()
    index_url = Workshop.objects.all()
    index_url = Register.objects.all()
    index_url = Language.objects.all()
    index_url = Payment.objects.all()
    index_url = Setting.objects.all()
    index_url = Articles.objects.all()

    context = {'index_url': index_url, }

    return render(request, 'index/list.html', context)


def index_detail(request):
    index_detail = Upload.objects.all()

    context = {'index_detail': index_detail, }

    return render(request, 'index/Speaker.html', context)

def index(request):
    index_index =Upload.objects.all()

    context = {'index': index, }


    return render(request, 'index/index.html', context)



def schedule(request):
     index_schedule = Upload.objects.all()

     context = {'index_schedule': index_schedule, }

     return render(request, 'index/Schedule part1.html', context)
