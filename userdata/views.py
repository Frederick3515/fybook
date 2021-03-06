# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import User
from django import forms

from django.http import HttpResponse


class UserForm(forms.Form):
    username=forms.CharField(label='用户名',max_length=20)
    password=forms.CharField(label='密码',widget=forms.PasswordInput())
# Create your views here.


def login(request):
    if request.method=='POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            get_username = uf.cleaned_data['username']
            get_password = uf.cleaned_data['password']
            result = User.objects.filter(username__exact=get_username, password__exact=get_password)
            if result:
                return HttpResponse(1)  #登录成功返回1
            else:
                return HttpResponse(0)  #用户名或密码错误返回0
        else :
              return HttpResponse(2)  #表单数据无效返回2


def signup(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            get_username = uf.cleaned_data['username']
            get_password = uf.cleaned_data['password']
            if User.objects.filter(username__exact=get_username):
                return HttpResponse(0)  #用户名存在返回0
            else:
                User.objects.create(username=get_username, password=get_password)
                return HttpResponse(1) #创建成功返回1

        else:
            return HttpResponse(2)  #表单数据无效返回2

def getuser(request):
    if request.method=='GET':
        get_user_id=request.GET['id']
        get_user_name=request.GET['username']
        get_user=User.objects.filter(id=0)

        if get_user_id=='0':
            get_user=User.objects.filter(username=get_user_name).values()
        elif get_user_name=='':
            get_user=User.objects.filter(id=get_user_id).values()

        if get_user:
            return JsonResponse(get_user[0])
        else:
            return JsonResponse({})

