from rest_framework import serializers

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


class SiteProfileSerializer(serializers.ModelSerializer):
    profile_image_url = serializers.SerializerMethodField()
    resume_url = serializers.SerializerMethodField()

    class Meta:
        model = SiteProfile
        fields = (
            "full_name",
            "professional_title",
            "hero_eyebrow",
            "hero_summary",
            "about_text",
            "work_philosophy",
            "technology_interests",
            "profile_image_url",
            "resume_url",
            "contact_email",
            "location",
            "availability_text",
            "contact_cta_title",
            "contact_cta_text",
        )

    def get_profile_image_url(self, obj):
        return self.build_absolute_file_url(obj.profile_image)

    def get_resume_url(self, obj):
        return self.build_absolute_file_url(obj.resume_file)

    def build_absolute_file_url(self, file_field):
        if not file_field:
            return None

        request = self.context.get("request")

        if request:
            return request.build_absolute_uri(file_field.url)

        return file_field.url


class SectionSettingsSerializer(serializers.ModelSerializer):
    label = serializers.CharField(
        source="get_key_display",
        read_only=True,
    )

    class Meta:
        model = SectionSettings
        fields = (
            "key",
            "label",
            "navigation_label",
            "eyebrow",
            "title",
            "description",
            "order",
        )


class SocialLinkSerializer(serializers.ModelSerializer):
    platform_label = serializers.CharField(
        source="get_platform_display",
        read_only=True,
    )

    class Meta:
        model = SocialLink
        fields = (
            "id",
            "platform",
            "platform_label",
            "label",
            "url",
            "icon_name",
            "open_in_new_tab",
            "order",
        )


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = (
            "id",
            "name",
            "slug",
            "icon_name",
            "official_url",
            "is_featured",
            "order",
        )


class TechnologyCategorySerializer(serializers.ModelSerializer):
    technologies = serializers.SerializerMethodField()

    class Meta:
        model = TechnologyCategory
        fields = (
            "id",
            "name",
            "slug",
            "description",
            "icon_name",
            "order",
            "technologies",
        )

    def get_technologies(self, obj):
        technologies = [
            technology
            for technology in obj.technologies.all()
            if technology.is_visible
        ]

        return TechnologySerializer(
            technologies,
            many=True,
            context=self.context,
        ).data


class ProfessionalStrengthSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalStrength
        fields = (
            "id",
            "title",
            "description",
            "icon_name",
            "order",
        )


class ExperienceSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(
        many=True,
        read_only=True,
    )

    period_label = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = (
            "id",
            "role",
            "company",
            "company_url",
            "location",
            "start_date",
            "end_date",
            "is_current",
            "period_label",
            "summary",
            "impact",
            "technologies",
            "order",
        )

    def get_period_label(self, obj):
        if not obj.start_date:
            return "Periodo no especificado"

        start = obj.start_date.strftime("%Y")

        if obj.is_current:
            return f"{start} — Actualidad"

        if obj.end_date:
            end = obj.end_date.strftime("%Y")
            return f"{start} — {end}"

        return start


class ProjectImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ProjectImage
        fields = (
            "id",
            "image_url",
            "alt_text",
            "caption",
            "order",
        )

    def get_image_url(self, obj):
        if not obj.image:
            return None

        request = self.context.get("request")

        if request:
            return request.build_absolute_uri(obj.image.url)

        return obj.image.url


class ProjectListSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(
        many=True,
        read_only=True,
    )

    cover_image_url = serializers.SerializerMethodField()

    status_label = serializers.CharField(
        source="get_status_display",
        read_only=True,
    )

    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "slug",
            "short_description",
            "role",
            "impact",
            "status",
            "status_label",
            "cover_image_url",
            "demo_url",
            "repository_url",
            "project_url",
            "is_repository_private",
            "is_featured",
            "started_at",
            "completed_at",
            "technologies",
            "order",
        )

    def get_cover_image_url(self, obj):
        if not obj.cover_image:
            return None

        request = self.context.get("request")

        if request:
            return request.build_absolute_uri(obj.cover_image.url)

        return obj.cover_image.url


class ProjectDetailSerializer(ProjectListSerializer):
    gallery = serializers.SerializerMethodField()

    class Meta(ProjectListSerializer.Meta):
        fields = ProjectListSerializer.Meta.fields + (
            "description",
            "gallery",
        )

    def get_gallery(self, obj):
        images = [
            image
            for image in obj.gallery.all()
            if image.is_visible
        ]

        return ProjectImageSerializer(
            images,
            many=True,
            context=self.context,
        ).data


class EducationSerializer(serializers.ModelSerializer):
    logo_url = serializers.SerializerMethodField()
    period_label = serializers.SerializerMethodField()

    class Meta:
        model = Education
        fields = (
            "id",
            "institution",
            "program",
            "location",
            "start_date",
            "end_date",
            "is_current",
            "period_label",
            "description",
            "institution_url",
            "logo_url",
            "order",
        )

    def get_logo_url(self, obj):
        if not obj.logo:
            return None

        request = self.context.get("request")

        if request:
            return request.build_absolute_uri(obj.logo.url)

        return obj.logo.url

    def get_period_label(self, obj):
        if not obj.start_date:
            return None

        start = obj.start_date.strftime("%Y")

        if obj.is_current:
            return f"{start} — Actualidad"

        if obj.end_date:
            return f"{start} — {obj.end_date.strftime('%Y')}"

        return start


class CertificationSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Certification
        fields = (
            "id",
            "name",
            "issuer",
            "issue_date",
            "expiration_date",
            "credential_id",
            "credential_url",
            "image_url",
            "order",
        )

    def get_image_url(self, obj):
        if not obj.image:
            return None

        request = self.context.get("request")

        if request:
            return request.build_absolute_uri(obj.image.url)

        return obj.image.url


class SidebarLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SidebarLink
        fields = (
            "id",
            "title",
            "description",
            "url",
            "icon_name",
            "badge_text",
            "open_in_new_tab",
            "order",
        )


class SeoSettingsSerializer(serializers.ModelSerializer):
    og_image_url = serializers.SerializerMethodField()

    class Meta:
        model = SeoSettings
        fields = (
            "site_title",
            "meta_description",
            "keywords",
            "canonical_url",
            "og_image_url",
            "robots_index",
        )

    def get_og_image_url(self, obj):
        if not obj.og_image:
            return None

        request = self.context.get("request")

        if request:
            return request.build_absolute_uri(obj.og_image.url)

        return obj.og_image.url


class PortfolioPublicSerializer(serializers.Serializer):
    profile = SiteProfileSerializer(
        allow_null=True,
    )

    sections = SectionSettingsSerializer(
        many=True,
    )

    social_links = SocialLinkSerializer(
        many=True,
    )

    technology_categories = TechnologyCategorySerializer(
        many=True,
    )

    strengths = ProfessionalStrengthSerializer(
        many=True,
    )

    experiences = ExperienceSerializer(
        many=True,
    )

    featured_projects = ProjectListSerializer(
        many=True,
    )

    education = EducationSerializer(
        many=True,
    )

    certifications = CertificationSerializer(
        many=True,
    )

    sidebar_links = SidebarLinkSerializer(
        many=True,
    )

    seo = SeoSettingsSerializer(
        allow_null=True,
    )