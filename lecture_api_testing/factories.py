import factory

from .models import City, Student, School


class CityFactory(factory.DjangoModelFactory):
    class Meta:
        model = City


class StudentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Student


class SchoolFactory(factory.DjangoModelFactory):
    class Meta:
        model = School
