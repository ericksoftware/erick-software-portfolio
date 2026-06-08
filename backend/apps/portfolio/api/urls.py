from django.urls import path

from .views import (
    PortfolioPublicAPIView,
    ProjectDetailAPIView,
    ProjectListAPIView,
)


urlpatterns = [
    path(
        "portfolio/",
        PortfolioPublicAPIView.as_view(),
        name="portfolio-public",
    ),
    path(
        "projects/",
        ProjectListAPIView.as_view(),
        name="project-list",
    ),
    path(
        "projects/<slug:slug>/",
        ProjectDetailAPIView.as_view(),
        name="project-detail",
    ),
]