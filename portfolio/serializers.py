from rest_framework import serializers
from portfolio.models import ProgrammingProject, ProgrammingImage, ArtProject, ArtImage
from rest_framework.settings import api_settings

class PProjectSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	title = serializers.CharField(required=True, allow_blank=False, max_length=50)
	workDate = serializers.DateField(format=api_settings.DATE_FORMAT, input_formats=None)
	languages = serializers.CharField(required=False, allow_blank=True, max_length=500)
	myParts = serializers.CharField(required=False, allow_blank=True, max_length=2000)
	sourceCode = serializers.CharField(required=False, allow_blank=True, max_length=100)
	desc = serializers.CharField(required=False, allow_blank=True, max_length=1000)
	
	def create(self, validated_data):
		return Portfolio.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.title = validated_data.get('title', instance.title)
		instance.workDate = validated_data.get('workDate', instance.workDate)
		instance.languages = validated_data.get('languages', instance.languages)
		instance.myParts = validated_data.get('myParts', instance.myParts)
		instance.sourceCode = validated_data.get('sourceCode', instance.sourceCode)
		instance.desc = validated_data.get('desc', instance.desc)
		instance.save()
		return instance