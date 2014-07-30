# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response

dic = {}


def home(request):

    return render_to_response('home.html', dic)
