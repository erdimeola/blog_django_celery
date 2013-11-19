#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from datetime import datetime
from uygulama import tasks

def index(request):
    zaman = datetime.now()
    tasks.zaman_ekle.delay(zaman)
    return HttpResponse('{"zaman":"'+str(zaman)+'"}', mimetype='application/json')