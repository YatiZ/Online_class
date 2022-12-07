from django.db import models

# Create your models here.

class StudentInfo(models.Model):
    image = models.ImageField(upload_to=None,default='spider.jpeg')
    name = models.CharField(max_length = 100)
    nickname = models.CharField(max_length=100)
    roll = models.IntegerField()
    address = models.TextField(max_length=200)
    phone = models.CharField(max_length=11)
    
    def __str__(self):
        return self.name
