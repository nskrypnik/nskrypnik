# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse

def index(request):
  return redirect('/blog/')

class Test(HttpResponse):

    def __init__(self, request):
        super(Test, self).__init__("Hello test!")
