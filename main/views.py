from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from .models import *
from django.views import generic
from django.core.urlresolvers import reverse
import json
from tangbofu.settings import *
#for processing post forms
from django.core.context_processors import csrf
from django.core.mail import send_mail #for contact page.
from django.views.decorators.csrf import csrf_exempt, csrf_protect, ensure_csrf_cookie
import sys
if sys.version_info[0]==2:
    reload(sys)
    sys.setdefaultencoding('utf8')

def home(request):
    return render(request, 'main/home.html', {})

def news_list(request, page=1):
    news_list = News.objects.all()
    context = {}
    context['news_list'] = news_list
    return render(request, 'main/news_list.html', context)

def news_detail(request, news_id=0):
    news = News.objects.get(id=news_id)
    context = {}
    context['news'] = news
    return render(request, 'main/news_detail.html', context)

def join_us(request):
    return render(request, 'main/join_us.html', {})

def contact_us(request):
    return render(request, 'main/contact_us.html', {})

def about(request):
    return render(request, 'main/about.html', {})

def send_email(request):
    return render(request, 'main/send_email.html', {})