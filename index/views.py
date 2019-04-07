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


def tabbed_layout(request):
    inedx_layout = Upload.objects.all()

    context = {'index_layout' : inedx_layout, }

    return render(request, 'index/tabbed-layout.html', context)

def error_page(request):
    index_404 = Upload.objects.all()

    context = {'index_404': index_404, }

    return  render(request, 'index/404-page.html', context)


def pricing_table(request):
    index_pricing = Upload.objects.all()

    context = {'index_pricing': index_pricing, }

    return render(request, 'index/pricing-table.html', context)

def coming_soon(request):
    index_coming = Upload.objects.all()

    context = {'index_coming': index_coming, }

    return render(request, 'index/coming-soon.html', context)

def content_us(request):
    index_content = Upload.objects.all()

    context = {'index_content': index_content, }

    return render(request, 'index/content-us', context)

def about_us(request):
    index_about = Upload.objects.all()

    context = {'index_about':index_about, }

    return render(request, 'index/about-us.html', context)

def blog(request):
    index_blog = Upload.objects.all()

    context = {'index_blog': index_blog, }

    return render(request, 'index/blog.html', context)
