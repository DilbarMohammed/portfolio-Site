from django.urls import path
from django.views.generic import RedirectView

from .views import AboutView, HomeView, ProjectListView


app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("projects/", ProjectListView.as_view(), name="projects"),
    path("services/", RedirectView.as_view(pattern_name="core:projects", permanent=True), name="services"),
]
