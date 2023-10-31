from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = "studyspots"
urlpatterns = [
    path("", views.index, name="index"),
    path("map/", views.map, name="map"),
    path("add/", views.add, name="add"),
    path("addNewLocation/", views.nonExistingLocation, name="addNewLocation"),
    path("addNewSpot/<int:location_id>/", views.addNewSpot, name="addNewSpot"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", views.profile, name="login"),
    path("load/", views.load, name="load"),
    path("load/spot/<int:location_id>", views.get_spot_data, name="get_spot_data"),
    path("confirmation/", views.confirmation, name="confirmation"),
]
