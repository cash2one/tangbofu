# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fields = ('title', 'desc', 'content', 'img_url')
    list_display = ('title', 'created', 'modified')
    list_filter = ('created',)
    date_hierarchy = 'created'