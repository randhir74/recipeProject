from django.db import models

# Create your models here.

class Student(models.Model):
    # id = models.AutoField() # Django add this ID automatically
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)


class Car(models.Model):
    car_name = models.CharField(max_length=200)
    speed = models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.car_name

class Product(models.Model):
    pass