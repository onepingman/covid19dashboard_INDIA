from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("indiamap", views.indiamap, name="indiamap" ),
    path("dailytrend/<str:state>", views.dailytrend, name="dailytrend"),
    path("datatable", views.datatable, name="datatable")
    ]