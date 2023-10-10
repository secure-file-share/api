# from django.urls import path
from rest_framework import routers
from . import viewsets  # , views

app_name = "organization"

# REST API ROUTER
router = routers.SimpleRouter()


# URLS
urlpatterns = []

urlpatterns += router.urls
