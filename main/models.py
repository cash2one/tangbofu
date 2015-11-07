# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
import datetime

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=50, default="标题")
    desc = models.CharField(max_length=255, default="描述")
    content = RichTextUploadingField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    def __unicode__(self):
        return self.title

    def was_created_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=30) <= self.created <= now

class Asset(models.Model):
    url = models.TextField(default="")

    def __unicode__(self):
        return str(self.url)
