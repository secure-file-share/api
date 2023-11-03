# from django.urls import path
from rest_framework import routers
from . import viewsets  # , views

app_name = "organization"

# REST API ROUTER
router = routers.SimpleRouter()

router.register(r'organization', viewsets.OrganizationViewSet,
                basename="organization")

# URLS
urlpatterns = []

urlpatterns += router.urls
