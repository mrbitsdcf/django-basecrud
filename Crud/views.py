#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.db.models.query import QuerySet

'''
Modulo BASE

@author Stefan Yohansson da Silva Areeira Pinto
@version 0.1

View base é o pai de todas as views do sistema com os metodos de criar,
listar, editar e excluir
'''

dic = {}

def create(request, formName, module, dic, template='basic/create.html', formData=None):
    forms = getattr(__import__(module, fromlist=['forms']), 'forms')
    methodtoCall = getattr(forms, formName)
    if request.POST:
        form = methodtoCall(request.POST, instance=formData)

        if form.is_valid():
            inserted = form.save()
            if request.POST['redirect']:
                return HttpResponseRedirect(reverse(request.POST['redirect'], args=[inserted.pk,]))
            else:
                # Redirecionar para view para ver os dados inseridos
                pass
                #return HttpResponseRedirect(reverse(request.POST['redirect'], args=[inserted.pk,]))
            # Adicionar redirecionamento vindo de id escondida no create

    else:

        if type(formData) is not dict:
            form = methodtoCall(instance=formData)
        elif type(formData) is dict:
            form = methodtoCall(formData)
        else:
            form = methodtoCall()

    dic.update({
        'form' : form
        })

    return render_to_response(template, dic, context_instance=RequestContext(request))

def update(request, formName, module, modelModule, modelName, dic, template='basic/create.html', formData=None):
    if modelModule is not None and modelName is not None:
        model = getattr(__import__(modelModule, fromlist=['models']), modelName)
        formData = model.objects.get(pk=dic['id'])

    return create(request, formName, module, dic, template, formData)

def read(request, module, modelName, fields, dic, template, options = None, data = None):
    model = getattr(__import__(module, fromlist=['models']), modelName)

    if data is None:
        rows = model.objects.all()
    else:
        rows = data

    options_html = {}

    for row in rows:
        options_html[row.id] = []
        for key, option in options.iteritems():
            arg_list = []
            for arg in option['args']:
                arg_list.append(getattr(row, arg))
            argscv = tuple(arg_list)
            options_html[row.id].append('<a href="' + reverse(option['href'], args=argscv) + '" class="' + option['class'] + '">' + option['label'] + '</a> ')

    dic.update({
        'rows' : rows,
        'fields': fields,
        'options': options_html
    })

    return render_to_response(template, dic, context_instance=RequestContext(request))

def detail(request, module, modelName, fields, dic, template, options = None, data = None):
    model = getattr(__import__(module, fromlist=['models']), modelName)

    if data is None:
        row = model.objects.get(pk=dic['id'])
    else:
        row = data

    options_html = []
    for key, option in options.iteritems():
        arg_list = []
        for arg in option['args']:
            arg_list.append(getattr(row, arg))
        argscv = tuple(arg_list)
        options_html.append('<a href="' + reverse(option['href'], args=argscv) + '" class="' + option['class'] + '">' + option['label'] + '</a> ')

    dic.update({
        'row' : row.__dict__,
        'fields' : fields,
        'options': options_html
    })

    return render_to_response(template, dic, context_instance=RequestContext(request))
