from django.db import models

# Create your models here.
class Clients(models.Model):
  name = models.CharField(max_length = 30)
  direction = models.CharField(max_length = 50)
  email = models.EmailField(max_length = 50)
  phone = models.CharField(max_length = 10)

class Items(models.Model):
  name = models.CharField(max_length = 30)
  section = models.CharField(max_length = 20)
  price = models.IntegerField()

class Order(models.Model):
  orderId = models.IntegerField()
  date = models.DateField()
  finished = models.BooleanField()
