# from django.urls import path
from rest_framework import routers
from . import viewsets  # , views

app_name = "fileshare"

# REST API ROUTER
router = routers.SimpleRouter()

router.register(r'fileshare', viewsets.FileShareViewSet, basename='fileshare')

# URLS
urlpatterns = []

urlpatterns += router.urls
