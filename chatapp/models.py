from django.db import models

class Conversation(models.Model):
    medicine = models.CharField(max_length=100,default='SOME STRING')
    symptoms=models.CharField(max_length=100,default='SOME STRING')
    dose=models.TextField()
    precautions=models.TextField()
    def __str__(self):
        return self.medicine
class suggestions(models.Model):
    input=models.CharField(max_length=100,default='SOME STRING')
    output=models.TextField()
    sug1=models.CharField(max_length=100,default='SOME STRING')
    sug2=models.CharField(max_length=100,default='SOME STRING')
    sug3=models.CharField(max_length=100,default='SOME STRING')
    sug4=models.CharField(max_length=100,default='SOME STRING')
    def __str__(self):
        return self.input
