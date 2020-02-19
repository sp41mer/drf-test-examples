from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CityViewSet, SchoolViewSet, StudentViewSet

router = DefaultRouter(trailing_slash=True)

router.register(r"cities", CityViewSet)
router.register(r"schools", SchoolViewSet)
router.register(r"students", StudentViewSet)
