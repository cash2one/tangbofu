# -*- coding: UTF-8 -*-
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
from django.core.paginator import Paginator
from django.utils.html import strip_tags

import sys
if sys.version_info[0]==2:
    reload(sys)
    sys.setdefaultencoding('utf8')

def home(request):
    seo = {
        'title': "北京男士养生会所_高端私人会所-唐伯府高端养生会所",
        'description': '唐伯府高端养生会是一家专门为高端男士打造的养生会所，总公司投资多元化，主要涉及：服务管理，影视制作，模特经纪，高端表演特制服务，公司在北京、上海、深圳均有高端私人会所。所有会所均设有茶道、香道、沉香木藏品展示，诚邀各界名流莅临品鉴。',
        'keywords': '高端养生会所,高端私人会所,北京男士养生会所,丝足会所,北京会所'
    }
    return render(request, 'main/home.html', {'seo': seo})

def news_list(request, current_page=1):
    seo = {
        'title': "唐伯府企业动态_动态新闻-唐伯府养生会所",
        'description': '唐伯府高端养生会是一家专门为高端男士打造的养生会所，提供高端养生相关资讯介绍，服务+专注打造北京最专业的高端私人会所。',
        'keywords': '北京养生会所,高端私人会所,北京男士养生会所,丝足会所,北京会所'
    }
    current_page = int(current_page)
    if current_page == '' or current_page < 1:
        current_page = 1
    news_list = News.objects.all()

    p = Paginator(news_list, 10)
    page = p.page(current_page)
    news_in_page = page.object_list
    startpage = current_page - 5
    if startpage < 1:
        startpage = 1
    endpage = startpage + 9
    if endpage >= p.num_pages:
        endpage = p.num_pages
    context = {}
    context['seo'] = seo
    context['news_list'] = news_in_page
    context['paginator'] = p
    context['page'] = page
    context['pagerange'] = xrange(startpage, endpage+1)
    return render(request, 'main/news_list.html', context)

def news_detail(request, news_id=0):
    news = News.objects.get(id=news_id)
    seo = {
        'title': "%s - 唐伯府养生会所" % news.title,
        'description': '唐伯府高端养生会是一家专门为高端男士打造的养生会所，%s' % strip_tags(news.content)[:100],
        'keywords': '%s，高端私人会所,北京男士养生会所,丝足会所,北京会所' % news.title
    }
    context = {}
    context['seo'] = seo
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