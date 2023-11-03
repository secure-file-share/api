# from django.urls import path
from rest_framework import routers
from . import viewsets  # , views

app_name = "client"

# REST API ROUTER
router = routers.SimpleRouter()

router.register(r'user', viewsets.ClientUserViewSet, basename="user")
router.register(r'search', viewsets.UserViewSet, basename="search")

# URLS
urlpatterns = []

urlpatterns += router.urls
