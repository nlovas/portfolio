# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import ProgrammingProject, ProgrammingImage
from portfolio.serializers import PProjectSerializer
from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
#from django.http import JsonResponse
import json
from django.core import serializers
from django.forms.models import model_to_dict

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

	#first get images and make a list. eg allimgs[0] = smc1.png url, smc2.png url, ...
	allImgs = ProgrammingImage.objects.all()
	allProjects = ProgrammingProject.objects.all()
	
	#images = [[]for i in range(len(allProjects))]
	#for img in allImgs:
	#	images[img.project.pk].append(img.image.url)

	images = []
	for img in allImgs:
		i = {
			'fk':img.project.pk,
			'imageurl':img.image.url
		}
		images.append(i)

	#then do the projects
	projects = []
	#projects = [[]for i in range(len(allProjects))]
	for proj in allProjects:
	#	projects[proj.pk].append(serializers.serialize('json',list(proj)))
		p = {
			'pk':proj.pk,
			'title': proj.title,
			'workDate':proj.workDate,
			'languages':proj.languages,
			'myParts':proj.myParts,
			'sourceCode':proj.sourceCode,
			'desc': proj.desc
		}
		#p = model_to_dict(proj)
		projects.append(p)
	#print projects
	#serialized = PProjectSerializer(allProjects, many=True)
	#projects = JSONRenderer().render(serialized.data)
	
	
	
	#projects = serializers.serialize('json', allProjects)###########
	#projects = JSONRenderer().render(serialized)
	
	
	
	return render(request,'programmingprojects.html',{'programmingprojects' : projects,'images': images})
	
#contact page
def contact(request):
	return render(request,'contact.html')