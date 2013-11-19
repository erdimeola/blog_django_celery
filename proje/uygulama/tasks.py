#!/usr/bin/python
# -*- coding: utf-8 -*-
from djcelery import celery
from uygulama.models import Zaman

@celery.task
def zaman_ekle(zaman):
    Zaman.objects.create(zaman=zaman)