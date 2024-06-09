from django.db import models

class Member(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    profession=models.CharField(max_length=100,default='SOME STRING')
    membership=models.CharField(max_length=100,default='SOME STRING')        
