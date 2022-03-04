from django.db import models

# Create your models here

class Result(models.Model):
    RESULT=(
        ('PASS','passed'),
        ('FAIL','failed')
    )
    name = models.CharField(max_length=30,unique=False)
    rollnumber=models.IntegerField(unique=True)
    resultStatus=models.CharField(max_length=8,choices=RESULT)
    grade=models.CharField(max_length=2,unique=False)

    def __str__(self):
        return f'Student-{self.name} with roll number {self.rollnumber} has {self.resultStatus}.'