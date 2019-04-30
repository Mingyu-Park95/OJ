from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.


class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True, primary_key=True, validators=[RegexValidator(regex='^[a-zA-Z0-9]+$')])
    fullName = models.CharField(max_length=20)


class ProblemsByUser(models.Model):
    pUsername = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    number = models.IntegerField()
    code = models.TextField()
    rightOrNot = models.BooleanField()
    submissionTime = models.DateTimeField(default=timezone.now)
    lang = models.CharField(max_length=20, verbose_name='language')
    runTime = models.FloatField()