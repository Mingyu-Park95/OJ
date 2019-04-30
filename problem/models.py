from django.db import models

# Create your models here.


class Problem(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    exTestCaseInput = models.TextField(verbose_name='exampleTestCaseInput')
    exTestCaseOutput = models.TextField(verbose_name='exampleTestCaseOutput')
    serverTestCaseInput = models.TextField()
    serverTestCaseOutput = models.TextField()
    numOfTry = models.IntegerField(default=0)
    numOfRight = models.IntegerField(default=0)
    image = models.ImageField()
    answerFile =models.FileField()

# 태그를 위해서 작성
# class tag(models.Model):
#     pass