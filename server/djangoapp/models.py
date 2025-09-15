# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    market = models.CharField(max_length=20)
    def __str__(self):
        return self.name

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealerid = models.IntegerField()
    name = models.CharField(max_length=50)
    CAR_TYPE = [
        ('SEDAN','Sedan'),
        ('COUPE','Coupe'),
        ('WAGON','Wagon'),
        ('TARGA','Targa'),
        ('CONVERT','Convertible'),
        ('SUV','SUV'),
        ('TRUCK','Truck'),
        ('UTE','Utility'),
        ('VAN','Van'),
    ]
    type = models.CharField(max_length=12, choices=CAR_TYPE, default='SEDAN')
    year = models.IntegerField()
    def __str__(self):
        return "{} {}".format(self.make, self.name)