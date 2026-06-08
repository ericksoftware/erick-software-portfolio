from django.db.models import Prefetch
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.portfolio.models import (
    Certification,
    Education,
    Experience,
    ProfessionalStrength,
    Project,
    ProjectImage,
    SectionSettings,
    SeoSettings,
    SidebarLink,
    SiteProfile,
    SocialLink,
    Technology,
    TechnologyCategory,
)

from .serializers import (
    PortfolioPublicSerializer,
    ProjectDetailSerializer,
    ProjectListSerializer,
)


def visible_technologies_queryset():
    return (
        Technology.objects
        .filter(is_visible=True)
        .select_related("category")
        .order_by("order", "id")
    )


def visible_project_images_queryset():
    return (
        ProjectImage.objects
        .filter(is_visible=True)
        .order_by("order", "id")
    )


def visible_projects_queryset():
    return (
        Project.objects
        .filter(is_visible=True)
        .prefetch_related(
            Prefetch(
                "technologies",
                queryset=visible_technologies_queryset(),
            ),
            Prefetch(
                "gallery",
                queryset=visible_project_images_queryset(),
            ),
        )
        .order_by("order", "id")
    )


class PortfolioPublicAPIView(APIView):
    """
    Entrega todo el contenido público necesario para construir
    la página principal del portfolio.
    """

    permission_classes = (AllowAny,)

    def get(self, request):
        technologies = visible_technologies_queryset()

        technology_categories = (
            TechnologyCategory.objects
            .filter(is_visible=True)
            .prefetch_related(
                Prefetch(
                    "technologies",
                    queryset=technologies,
                )
            )
            .order_by("order", "id")
        )

        experiences = (
            Experience.objects
            .filter(is_visible=True)
            .prefetch_related(
                Prefetch(
                    "technologies",
                    queryset=visible_technologies_queryset(),
                )
            )
            .order_by("order", "id")
        )

        featured_projects = (
            visible_projects_queryset()
            .filter(is_featured=True)
        )

        data = {
            "profile": SiteProfile.objects.first(),
            "sections": (
                SectionSettings.objects
                .filter(is_visible=True)
                .order_by("order", "id")
            ),
            "social_links": (
                SocialLink.objects
                .filter(is_visible=True)
                .order_by("order", "id")
            ),
            "technology_categories": technology_categories,
            "strengths": (
                ProfessionalStrength.objects
                .filter(is_visible=True)
                .order_by("order", "id")
            ),
            "experiences": experiences,
            "featured_projects": featured_projects,
            "education": (
                Education.objects
                .filter(is_visible=True)
                .order_by("order", "id")
            ),
            "certifications": (
                Certification.objects
                .filter(is_visible=True)
                .order_by("order", "id")
            ),
            "sidebar_links": (
                SidebarLink.objects
                .filter(is_visible=True)
                .order_by("order", "id")
            ),
            "seo": SeoSettings.objects.first(),
        }

        serializer = PortfolioPublicSerializer(
            instance=data,
            context={
                "request": request,
            },
        )

        return Response(serializer.data)


class ProjectListAPIView(ListAPIView):
    """
    Lista pública de proyectos visibles.
    """

    serializer_class = ProjectListSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return visible_projects_queryset()


class ProjectDetailAPIView(RetrieveAPIView):
    """
    Detalle público de un proyecto visible.
    """

    serializer_class = ProjectDetailSerializer
    permission_classes = (AllowAny,)
    lookup_field = "slug"

    def get_queryset(self):
        return visible_projects_queryset()