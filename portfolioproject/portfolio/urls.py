from portfolio import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("side-project", views.side_project, name="side-project"),
]
