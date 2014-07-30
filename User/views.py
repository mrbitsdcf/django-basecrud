# -*- coding: utf-8 -*-

# from django.shortcuts import render_to_response
from Crud import views as baseView

dic = {}


def userCreate(request):
    dic.update({
        'title_page': 'Add a User',
        'redirect': 'user-view'
    })

    formName = 'userForm'
    module = 'User'
    template = 'basic/create.html'

    return baseView.create(request, formName, module, dic, template)


def userUpdate(request, id):
    dic.update({
        'title_page': 'Edit a User',
        'id' : id,
        'redirect': 'user-view'
    })

    formName = 'userForm'
    formModule = 'User'
    template = 'basic/create.html'

    modelModule = 'django.contrib.auth.models'
    modelName = 'User'

    formData = {
        'username': 'ashudauhduashd'
    }

    return baseView.update(request, formName, formModule, modelModule, modelName, dic, template, formData)

def userRead(request):
    dic.update({
        'title_page': 'List users',
    })

    module = 'django.contrib.auth.models'
    modelName = 'User'
    template = 'basic/read.html'

    fields = ['username', 'password']

    data = None

    options = {
        'editar' : {'href': 'user-update', 'class': 'btn btn-info', 'label': 'Editar', 'args': ['id']},
        #{'link': 'user-update', 'label': 'Editar', 'args': {'id'}},
    }

    return baseView.read(request, module, modelName, fields, dic, template, options, data)

def userView(request):
    dic.update({
        'title_page': 'View users',
    })

    module = 'django.contrib.auth.models'
    modelName = 'User'
    template = 'basic/read.html'

    fields = ['username', 'password']

    data = None

    options = {
        'editar' : {'link': 'user-update', 'label': 'Editar'},
        #{'link': 'user-update', 'label': 'Editar', 'args': {'id'}},
    }

    return baseView.read(request, module, modelName, fields, dic, template, options, data)
