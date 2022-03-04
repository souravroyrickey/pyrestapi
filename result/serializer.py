from rest_framework import serializers
from .models import Result

class ResultSerializer(serializers.ModelSerializer):

	class Meta:
        	model = Result
        	fields = ['rollnumber','name','resultStatus','grade']


class ResultDetailSerializer(serializers.ModelSerializer):
	name = serializers.CharField(max_length=30)
	rollnumber = serializers.IntegerField()
	resultStatus = serializers.CharField(max_length=8)
	grade = serializers.CharField(max_length=2)

	class Meta:
        	model = Result
        	fields = ['rollnumber','name','resultStatus','grade']

class UpdateGradeSerializer(serializers.ModelSerializer):
	resultStatus = serializers.HiddenField(default='PASS')
	grade = serializers.CharField(max_length=2)

	class Meta:
		model = Result
		fields = ['resultStatus', 'grade']