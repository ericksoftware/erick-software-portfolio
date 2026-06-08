from django.contrib import admin

from .models import (
    Certification,
    Education,
    Experience,
    Project,
    ProjectImage,
    SectionSettings,
    SeoSettings,
    SidebarLink,
    SiteProfile,
    SocialLink,
    Technology,
    TechnologyCategory,
    ProfessionalStrength,
)


class SingletonAdminMixin:
    """
    Impide crear más de un registro para configuraciones únicas.
    """

    def has_add_permission(self, request):
        return not self.model.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(SiteProfile)
class SiteProfileAdmin(SingletonAdminMixin, admin.ModelAdmin):
    fieldsets = (
        (
            "Identidad profesional",
            {
                "fields": (
                    "full_name",
                    "professional_title",
                    "hero_eyebrow",
                    "hero_summary",
                    "profile_image",
                    "resume_file",
                )
            },
        ),
        (
            "Sobre mí",
            {
                "fields": (
                    "about_text",
                    "work_philosophy",
                    "technology_interests",
                )
            },
        ),
        (
            "Contacto",
            {
                "fields": (
                    "contact_email",
                    "location",
                    "availability_text",
                    "contact_cta_title",
                    "contact_cta_text",
                )
            },
        ),
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(SectionSettings)
class SectionSettingsAdmin(admin.ModelAdmin):
    list_display = (
        "key",
        "title",
        "navigation_label",
        "order",
        "is_visible",
    )

    list_editable = (
        "order",
        "is_visible",
    )

    list_filter = ("is_visible",)

    search_fields = (
        "title",
        "description",
        "navigation_label",
    )

    ordering = (
        "order",
        "id",
    )


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = (
        "label",
        "platform",
        "url",
        "order",
        "is_visible",
    )

    list_editable = (
        "order",
        "is_visible",
    )

    list_filter = (
        "platform",
        "is_visible",
    )

    search_fields = (
        "label",
        "url",
    )


class TechnologyInline(admin.TabularInline):
    model = Technology
    extra = 0

    fields = (
        "name",
        "slug",
        "icon_name",
        "is_featured",
        "order",
        "is_visible",
    )


@admin.register(TechnologyCategory)
class TechnologyCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "order",
        "is_visible",
    )

    list_editable = (
        "order",
        "is_visible",
    )

    search_fields = (
        "name",
        "slug",
    )

    inlines = (TechnologyInline,)


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "is_featured",
        "order",
        "is_visible",
    )

    list_editable = (
        "is_featured",
        "order",
        "is_visible",
    )

    list_filter = (
        "category",
        "is_featured",
        "is_visible",
    )

    search_fields = (
        "name",
        "slug",
    )

    autocomplete_fields = ("category",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = (
        "role",
        "company",
        "start_date",
        "end_date",
        "is_current",
        "order",
        "is_visible",
    )

    list_editable = (
        "order",
        "is_visible",
    )

    list_filter = (
        "is_current",
        "is_visible",
    )

    search_fields = (
        "role",
        "company",
        "summary",
        "impact",
    )

    filter_horizontal = ("technologies",)


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 0

    fields = (
        "image",
        "alt_text",
        "caption",
        "order",
        "is_visible",
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "is_featured",
        "order",
        "is_visible",
    )

    list_editable = (
        "is_featured",
        "order",
        "is_visible",
    )

    list_filter = (
        "status",
        "is_featured",
        "is_visible",
    )

    search_fields = (
        "title",
        "short_description",
        "description",
        "impact",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }

    filter_horizontal = ("technologies",)

    inlines = (ProjectImageInline,)


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = (
        "project",
        "alt_text",
        "order",
        "is_visible",
    )

    list_editable = (
        "order",
        "is_visible",
    )

    list_filter = (
        "project",
        "is_visible",
    )

    search_fields = (
        "project__title",
        "alt_text",
        "caption",
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        "program",
        "institution",
        "start_date",
        "end_date",
        "is_current",
        "order",
        "is_visible",
    )

    list_editable = (
        "order",
        "is_visible",
    )

    list_filter = (
        "is_current",
        "is_visible",
    )

    search_fields = (
        "program",
        "institution",
        "description",
    )


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "issuer",
        "issue_date",
        "expiration_date",
        "order",
        "is_visible",
    )

    list_editable = (
        "order",
        "is_visible",
    )

    list_filter = (
        "issuer",
        "is_visible",
    )

    search_fields = (
        "name",
        "issuer",
        "credential_id",
    )


@admin.register(SidebarLink)
class SidebarLinkAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "url",
        "badge_text",
        "open_in_new_tab",
        "order",
        "is_visible",
    )

    list_editable = (
        "order",
        "is_visible",
    )

    list_filter = (
        "open_in_new_tab",
        "is_visible",
    )

    search_fields = (
        "title",
        "description",
        "url",
    )

@admin.register(ProfessionalStrength)
class ProfessionalStrengthAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "order",
        "is_visible",
    )

    list_editable = (
        "order",
        "is_visible",
    )

    search_fields = (
        "title",
        "description",
    )

    ordering = (
        "order",
        "id",
    )

@admin.register(SeoSettings)
class SeoSettingsAdmin(SingletonAdminMixin, admin.ModelAdmin):
    fieldsets = (
        (
            "Metadatos",
            {
                "fields": (
                    "site_title",
                    "meta_description",
                    "keywords",
                    "canonical_url",
                )
            },
        ),
        (
            "Redes sociales y buscadores",
            {
                "fields": (
                    "og_image",
                    "robots_index",
                )
            },
        ),
    )