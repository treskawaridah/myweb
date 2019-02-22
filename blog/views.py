# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from blog.models import Artikel

# Create your views here.

def index(request):
    buah= ['Apel', 'Jeruk', 'Durian']
    return render(request, 'index.html', {'buah':buah})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html') 

def blog(request):
    # select * from Artikel
    blogs = Artikel.objects.all()
    return render(request, 'blog.html', {'blogs':blogs})    
