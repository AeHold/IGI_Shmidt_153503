from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Form(models.Model):
    name = models.TextField(max_length=20,db_index=True)

class Hall(models.Model):
    name = models.CharField(max_length=50)
    floor = models.IntegerField()
    square = models.FloatField()

class Exponate(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    author = models.TextField(max_length=50)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    photo = models.ImageField()
    worker = models.ForeignKey(User, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    receipt_date = models.DateField()

class Post(models.Model):
    name = models.CharField(max_length=30)
    user = models.ManyToManyField(User, related_name="post")

class Exhibition(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)

class Excursion(models.Model):
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE)
    date = models.DateTimeField()
    guide = models.ForeignKey(User, on_delete=models.CASCADE)


    







