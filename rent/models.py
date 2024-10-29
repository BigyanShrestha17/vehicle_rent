from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CarType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    car_type = models.ForeignKey(CarType, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/vehicles/', default="default.jpg")

    def __str__(self):
        return self.name
