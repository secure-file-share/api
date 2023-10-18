from django.urls import path
from rest_framework import routers
from . import viewsets, views

app_name = "alpha"

# REST API ROUTER
router = routers.SimpleRouter()


# URLS
urlpatterns = [
    path("", views.HomeView.as_view(), name="home")
]

urlpatterns += router.urls
