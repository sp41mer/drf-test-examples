from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import ModelViewSet

from .models import City, School, Student
from .serializers import CitySerializer, SchoolSerializer, StudentSerializer


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class SchoolViewSet(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
