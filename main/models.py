# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
import datetime

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=50, default=u"标题", verbose_name=u"文章标题")
    desc = models.CharField(max_length=255, default=u"描述", verbose_name=u"文章描述")
    img_url = models.CharField(max_length=255, default=u"配图", verbose_name=u"文章配图")
    content = RichTextUploadingField(verbose_name=u"正文")
    created = models.DateTimeField(auto_now_add=True, verbose_name=u"发布时间")
    modified = models.DateTimeField(auto_now=True, verbose_name=u"修改时间")

    def __unicode__(self):
        return self.title

    def was_created_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=30) <= self.created <= now

    class Meta:
        verbose_name = '资讯'
        verbose_name_plural = '资讯'

class Asset(models.Model):
    url = models.TextField(default="")

    def __unicode__(self):
        return str(self.url)
