# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

#homepage
def home(request):
	return render(request,'mainPage.html')

#redirect to homepage if no /
def slash(request):
	return redirect(reverse(home))
	
#art page
def art(request):
	return render(request,'artndesign.html')
	
#programming projects page
def programming(request):
	return render(request,'programmingprojects.html')
	
#contact page
def contact(request):
	return render(request,'contact.html')