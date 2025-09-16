from django.db import models
# from django.utils.timezone import now
# from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    market = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealerid = models.IntegerField()
    name = models.CharField(max_length=50)
    CAR_TYPE = [
        ('SEDAN', 'Sedan'),
        ('COUPE', 'Coupe'),
        ('WAGON', 'Wagon'),
        ('TARGA', 'Targa'),
        ('CONVERT', 'Convertible'),
        ('SUV', 'SUV'),
        ('TRUCK', 'Truck'),
        ('UTE', 'Utility'),
        ('VAN', 'Van'),
    ]
    type = models.CharField(max_length=12, choices=CAR_TYPE, default='SEDAN')
    year = models.IntegerField()

    def __str__(self):
        return "{} {}".format(self.make, self.name)
