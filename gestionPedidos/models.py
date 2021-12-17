from django.db import models

# Create your models here.
class Clients(models.Model):
  name = models.CharField(max_length = 30)
  direction = models.CharField(max_length = 50)
  email = models.EmailField(max_length = 50)
  phone = models.CharField(max_length = 10)

  def __str__(self):
    return f'name: {self.name} - direction: {self.direction} - email: {self.email} - phone: {self.phone}'

class Items(models.Model):
  name = models.CharField(max_length = 30)
  section = models.CharField(max_length = 20)
  price = models.IntegerField()

  def __str__(self):
    return f'name: {self.name} - section: {self.section} - price: {self.price}\n'

class Order(models.Model):
  orderId = models.IntegerField()
  date = models.DateField()
  finished = models.BooleanField()

  def __str__(self):
    return f'orderId: {self.orderId} - date: {self.date} - finished: {self.finished}\n'

  def __str__(self):
    return f'name: {self.name} - section: {self.section} - price: {self.price}\n'
