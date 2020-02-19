from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APISimpleTestCase, APITransactionTestCase
from rest_framework.test import APIRequestFactory

from .models import City, School, Student
from .factories import CityFactory, SchoolFactory, StudentFactory
from .views import CityViewSet, SchoolViewSet, StudentViewSet


# APISimpleTestCase (doesn't work with db)
class TestCaseForCitySimple(APISimpleTestCase):
    def test_create_city_request_factory(self):
        city = CityFactory.build(name="Test", population=1)
        self.assertEqual(city.name, "Test")


# APITestCase (allows to work with db)
class TestCaseForCity(APITestCase):

    # Testing via request factory
    def test_get_city_request_factory(self):
        city = CityFactory(name="Test", population=1)
        request_factory = APIRequestFactory()
        request = request_factory.get("/api/cities/")
        city_view = CityViewSet.as_view({"get": "list"})
        response = city_view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_city_request_factory(self):
        request_factory = APIRequestFactory()
        request = request_factory.post(
            "/api/cities/", {"name": "Test", "population": 1}, format="json"
        )
        city_view = CityViewSet.as_view({"post": "create"})
        response = city_view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Testing via api client
    def test_get_city_api_client(self):
        city = CityFactory(name="Test", population=1)
        response = self.client.get("/api/cities/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_city_api_client(self):
        response = self.client.post(
            "/api/cities/", data={"name": "Test", "population": 1}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Will fail
    def test_transactional_case_for_city(self):
        CityFactory(name="Test", population=1)
        city = City.objects.first()
        city.set_population_to_zero()
        self.assertEqual(city.name, "Died")


class TestCaseForCityWithTransaction(APITransactionTestCase):
    def test_transactional_case_for_city(self):
        CityFactory(name="Test", population=1)
        city = City.objects.first()
        city.set_population_to_zero()
        self.assertEqual(city.name, "Died")
