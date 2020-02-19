from django.db import models


class City(models.Model):
    name = models.TextField()
    population = models.BigIntegerField()


class School(models.Model):
    name = models.TextField()
    number = models.SmallIntegerField()
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)


class Student(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
