# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import ProgrammingProject, ProgrammingImage
from portfolio.serializers import PProjectSerializer
from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
from django.http import JsonResponse
import json


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
	
	images = [[]for i in range(len(allProjects))]
	for img in allImgs:
		images[img.project.pk].append(img.image.url)
	
	#then do the projects
	#projects = [[]for i in range(len(allProjects))]
	#for proj in allProjects:
	#	projects[proj.pk].append(serializers.serialize('json',list(proj)))
	
	serialized = PProjectSerializer(allProjects, many=True)
	projects = JSONRenderer().render(serialized.data)
	
	#data = {projects,images}
	
	#projects = serializers.serialize('json', list(allProjects))
	#projects = json.dumps(list(allProjects), cls=DjangoJSONEncoder) 
	return render(request,'programmingprojects.html',{'programmingprojects' : json.dumps(projects),'images': images})
	#return JsonResponse({'projects': projects,'images': images},status=200)
	#return HttpResponse(data, content_type='application/json')
	
#contact page
def contact(request):
	return render(request,'contact.html')