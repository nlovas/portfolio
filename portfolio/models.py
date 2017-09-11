# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#there will be a general page for art & programming, then a more specific page for each project telling more about it
###inspiration: https://zachhoefler.com/

#programming:
# title, approx date worked on, language(s), goals & reqs, screenshots, github location, parts I did/learned
class ProgrammingProject(models.Model):
	title = models.CharField(max_length=50)
	workDate = models.CharField(max_length=50)
	languages = models.CharField(max_length=500)
	myParts = models.CharField(max_length=2000)
	sourceCode = models.CharField(max_length=100)
	desc = models.CharField(max_length=1000)
	

#for having multiple screenshots in programming projects
class ProgrammingImage(models.Model):
	project = models.ForeignKey(ProgrammingProject, related_name='images')
	image = models.ImageField()

#art
#title, approx date, set of images(1 or more), goals & reqs, desc
class ArtProject(models.Model):
	title = models.CharField(max_length=50)
	workDate = models.CharField(max_length=50)
	requirements = models.CharField(max_length=1000)
	desc = models.CharField(max_length=1000)

class ArtImage(models.Model):
	project = models.ForeignKey(ArtProject, related_name='images')
	image = models.ImageField()