from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

from apps.common.models import OrderedVisibleModel, TimeStampedModel


class SiteProfile(TimeStampedModel):
    """
    Información principal del propietario del portfolio.

    Este modelo está diseñado para contener un solo registro.
    """

    full_name = models.CharField(
        max_length=160,
        default="Erick Manuel Rodríguez López",
        verbose_name="nombre completo",
    )

    professional_title = models.CharField(
        max_length=160,
        default="Software Engineer / Full-Stack Developer",
        verbose_name="título profesional",
    )

    hero_eyebrow = models.CharField(
        max_length=120,
        blank=True,
        default="Ingeniero de Software",
        verbose_name="texto superior del hero",
    )

    hero_summary = models.TextField(
        default=(
            "Desarrollo aplicaciones web modernas, escalables y bien diseñadas, "
            "combinando experiencia full-stack, calidad de software y una "
            "mentalidad orientada a resolver problemas reales."
        ),
        verbose_name="resumen principal",
    )

    about_text = models.TextField(
        blank=True,
        verbose_name="sobre mí",
    )

    work_philosophy = models.TextField(
        blank=True,
        verbose_name="filosofía de trabajo",
    )

    technology_interests = models.TextField(
        blank=True,
        verbose_name="intereses tecnológicos",
    )

    profile_image = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True,
        verbose_name="fotografía de perfil",
    )

    resume_file = models.FileField(
        upload_to="resume/",
        blank=True,
        null=True,
        verbose_name="currículum",
    )

    contact_email = models.EmailField(
        blank=True,
        verbose_name="correo de contacto",
    )

    location = models.CharField(
        max_length=150,
        blank=True,
        default="Tijuana, Baja California, México",
        verbose_name="ubicación",
    )

    availability_text = models.CharField(
        max_length=180,
        blank=True,
        default="Disponible para nuevas oportunidades profesionales",
        verbose_name="disponibilidad",
    )

    contact_cta_title = models.CharField(
        max_length=180,
        blank=True,
        default="Construyamos algo de valor",
        verbose_name="título de contacto",
    )

    contact_cta_text = models.TextField(
        blank=True,
        default=(
            "Estoy abierto a oportunidades donde pueda aportar experiencia, "
            "seguir creciendo y colaborar en productos de calidad."
        ),
        verbose_name="texto de contacto",
    )

    class Meta:
        verbose_name = "perfil del sitio"
        verbose_name_plural = "perfil del sitio"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return None

    def __str__(self) -> str:
        return self.full_name


class SectionSettings(OrderedVisibleModel):
    """
    Permite modificar títulos, descripciones, visibilidad y orden
    de las secciones principales.
    """

    class SectionKey(models.TextChoices):
        HERO = "hero", "Hero"
        ABOUT = "about", "Sobre mí"
        STACK = "stack", "Stack tecnológico"
        EXPERIENCE = "experience", "Experiencia"
        PROJECTS = "projects", "Proyectos"
        EDUCATION = "education", "Educación"
        CONTACT = "contact", "Contacto"

    key = models.CharField(
        max_length=30,
        choices=SectionKey.choices,
        unique=True,
        verbose_name="sección",
    )

    navigation_label = models.CharField(
        max_length=80,
        blank=True,
        verbose_name="texto en navegación",
    )

    eyebrow = models.CharField(
        max_length=120,
        blank=True,
        verbose_name="texto superior",
    )

    title = models.CharField(
        max_length=180,
        verbose_name="título",
    )

    description = models.TextField(
        blank=True,
        verbose_name="descripción",
    )

    class Meta(OrderedVisibleModel.Meta):
        verbose_name = "configuración de sección"
        verbose_name_plural = "configuración de secciones"

    def __str__(self) -> str:
        return self.get_key_display()


class SocialLink(OrderedVisibleModel):
    class Platform(models.TextChoices):
        GITHUB = "github", "GitHub"
        LINKEDIN = "linkedin", "LinkedIn"
        EMAIL = "email", "Correo electrónico"
        WEBSITE = "website", "Sitio web"
        X = "x", "X / Twitter"
        INSTAGRAM = "instagram", "Instagram"
        OTHER = "other", "Otro"

    platform = models.CharField(
        max_length=30,
        choices=Platform.choices,
        verbose_name="plataforma",
    )

    label = models.CharField(
        max_length=100,
        verbose_name="etiqueta",
    )

    url = models.CharField(
        max_length=500,
        verbose_name="dirección",
        help_text="Puede ser una URL, mailto:correo@dominio.com u otra dirección.",
    )

    icon_name = models.CharField(
        max_length=80,
        blank=True,
        verbose_name="nombre del icono",
        help_text="Ejemplo: github, linkedin o mail.",
    )

    open_in_new_tab = models.BooleanField(
        default=True,
        verbose_name="abrir en otra pestaña",
    )

    class Meta(OrderedVisibleModel.Meta):
        verbose_name = "enlace social"
        verbose_name_plural = "enlaces sociales"

    def __str__(self) -> str:
        return self.label


class TechnologyCategory(OrderedVisibleModel):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="nombre",
    )

    slug = models.SlugField(
        max_length=120,
        unique=True,
        verbose_name="identificador",
    )

    description = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="descripción",
    )

    icon_name = models.CharField(
        max_length=80,
        blank=True,
        verbose_name="icono",
    )

    class Meta(OrderedVisibleModel.Meta):
        verbose_name = "categoría tecnológica"
        verbose_name_plural = "categorías tecnológicas"

    def __str__(self) -> str:
        return self.name


class Technology(OrderedVisibleModel):
    category = models.ForeignKey(
        TechnologyCategory,
        on_delete=models.PROTECT,
        related_name="technologies",
        verbose_name="categoría",
    )

    name = models.CharField(
        max_length=100,
        verbose_name="nombre",
    )

    slug = models.SlugField(
        max_length=120,
        verbose_name="identificador",
    )

    icon_name = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="icono",
        help_text="Ejemplo: react, python, spring, postgresql.",
    )

    official_url = models.URLField(
        blank=True,
        verbose_name="sitio oficial",
    )

    is_featured = models.BooleanField(
        default=False,
        verbose_name="destacada",
    )

    class Meta(OrderedVisibleModel.Meta):
        verbose_name = "tecnología"
        verbose_name_plural = "tecnologías"
        constraints = [
            models.UniqueConstraint(
                fields=("category", "slug"),
                name="unique_technology_slug_per_category",
            ),
        ]

    def __str__(self) -> str:
        return self.name


class Experience(OrderedVisibleModel):
    role = models.CharField(
        max_length=160,
        verbose_name="puesto",
    )

    company = models.CharField(
        max_length=160,
        verbose_name="empresa u organización",
    )

    company_url = models.URLField(
        blank=True,
        verbose_name="sitio de la empresa",
    )

    location = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="ubicación",
    )

    start_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="fecha de inicio",
    )

    end_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="fecha de finalización",
    )

    is_current = models.BooleanField(
        default=False,
        verbose_name="trabajo actual",
    )

    summary = models.TextField(
        verbose_name="descripción",
    )

    impact = models.TextField(
        blank=True,
        verbose_name="impacto y resultados",
    )

    technologies = models.ManyToManyField(
        Technology,
        blank=True,
        related_name="experiences",
        verbose_name="tecnologías",
    )

    class Meta(OrderedVisibleModel.Meta):
        verbose_name = "experiencia"
        verbose_name_plural = "experiencias"

    def clean(self):
        super().clean()

        if self.is_current and self.end_date:
            raise ValidationError(
                {
                    "end_date": (
                        "Una experiencia marcada como actual no debe tener "
                        "fecha de finalización."
                    )
                }
            )

        if (
                self.start_date
                and self.end_date
                and self.end_date < self.start_date
            ):
            raise ValidationError(
                {
                    "end_date": (
                        "La fecha de finalización no puede ser anterior "
                        "a la fecha de inicio."
                    )
                }
            )

    def __str__(self) -> str:
        return f"{self.role} — {self.company}"


class Project(OrderedVisibleModel):
    class Status(models.TextChoices):
        DEVELOPMENT = "development", "En desarrollo"
        ACTIVE = "active", "Activo"
        COMPLETED = "completed", "Completado"
        MAINTENANCE = "maintenance", "En mantenimiento"
        ARCHIVED = "archived", "Archivado"

    title = models.CharField(
        max_length=180,
        verbose_name="título",
    )

    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name="identificador",
    )

    short_description = models.CharField(
        max_length=300,
        verbose_name="descripción corta",
    )

    description = models.TextField(
        verbose_name="descripción completa",
    )

    role = models.CharField(
        max_length=160,
        blank=True,
        verbose_name="rol desempeñado",
    )

    impact = models.TextField(
        blank=True,
        verbose_name="impacto o resultados",
    )

    status = models.CharField(
        max_length=30,
        choices=Status.choices,
        default=Status.COMPLETED,
        verbose_name="estado",
    )

    cover_image = models.ImageField(
        upload_to="projects/covers/",
        blank=True,
        null=True,
        verbose_name="imagen de portada",
    )

    demo_url = models.URLField(
        blank=True,
        verbose_name="demostración",
    )

    repository_url = models.URLField(
        blank=True,
        verbose_name="repositorio",
    )

    project_url = models.URLField(
        blank=True,
        verbose_name="URL o subdominio del proyecto",
    )

    is_repository_private = models.BooleanField(
        default=False,
        verbose_name="repositorio privado",
    )

    is_featured = models.BooleanField(
        default=False,
        db_index=True,
        verbose_name="proyecto destacado",
    )

    started_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="fecha de inicio",
    )

    completed_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="fecha de finalización",
    )

    technologies = models.ManyToManyField(
        Technology,
        blank=True,
        related_name="projects",
        verbose_name="tecnologías",
    )

    class Meta(OrderedVisibleModel.Meta):
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"

    def clean(self):
        super().clean()

        if (
            self.started_at
            and self.completed_at
            and self.completed_at < self.started_at
        ):
            raise ValidationError(
                {
                    "completed_at": (
                        "La fecha de finalización no puede ser anterior "
                        "a la fecha de inicio."
                    )
                }
            )

    def get_absolute_url(self):
        return reverse(
            "project-detail",
            kwargs={"slug": self.slug},
        )

    def __str__(self) -> str:
        return self.title


class ProjectImage(OrderedVisibleModel):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="gallery",
        verbose_name="proyecto",
    )

    image = models.ImageField(
        upload_to="projects/gallery/",
        verbose_name="imagen",
    )

    alt_text = models.CharField(
        max_length=180,
        verbose_name="texto alternativo",
        help_text="Describe la imagen para accesibilidad.",
    )

    caption = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="descripción",
    )

    class Meta(OrderedVisibleModel.Meta):
        verbose_name = "imagen de proyecto"
        verbose_name_plural = "imágenes de proyectos"

    def __str__(self) -> str:
        return f"{self.project.title} — {self.alt_text}"


class Education(OrderedVisibleModel):
    institution = models.CharField(
        max_length=180,
        verbose_name="institución",
    )

    program = models.CharField(
        max_length=180,
        verbose_name="programa o carrera",
    )

    location = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="ubicación",
    )

    start_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="fecha de inicio",
    )

    end_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="fecha de finalización",
    )

    is_current = models.BooleanField(
        default=False,
        verbose_name="actualmente estudiando",
    )

    description = models.TextField(
        blank=True,
        verbose_name="descripción",
    )

    institution_url = models.URLField(
        blank=True,
        verbose_name="sitio de la institución",
    )

    logo = models.ImageField(
        upload_to="education/",
        blank=True,
        null=True,
        verbose_name="logotipo",
    )

    class Meta(OrderedVisibleModel.Meta):
        verbose_name = "educación"
        verbose_name_plural = "educación"

    def clean(self):
        super().clean()

        if self.is_current and self.end_date:
            raise ValidationError(
                {
                    "end_date": (
                        "Un programa actual no debe tener fecha "
                        "de finalización."
                    )
                }
            )

        if (
            self.start_date
            and self.end_date
            and self.end_date < self.start_date
        ):
            raise ValidationError(
                {
                    "end_date": (
                        "La fecha de finalización no puede ser anterior "
                        "a la fecha de inicio."
                    )
                }
            )

    def __str__(self) -> str:
        return f"{self.program} — {self.institution}"


class Certification(OrderedVisibleModel):
    name = models.CharField(
        max_length=180,
        verbose_name="certificación",
    )

    issuer = models.CharField(
        max_length=180,
        verbose_name="institución emisora",
    )

    issue_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="fecha de emisión",
    )

    expiration_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="fecha de expiración",
    )

    credential_id = models.CharField(
        max_length=180,
        blank=True,
        verbose_name="identificador de credencial",
    )

    credential_url = models.URLField(
        blank=True,
        verbose_name="URL de la credencial",
    )

    image = models.ImageField(
        upload_to="certifications/",
        blank=True,
        null=True,
        verbose_name="imagen",
    )

    class Meta(OrderedVisibleModel.Meta):
        verbose_name = "certificación"
        verbose_name_plural = "certificaciones"

    def clean(self):
        super().clean()

        if (
            self.issue_date
            and self.expiration_date
            and self.expiration_date < self.issue_date
        ):
            raise ValidationError(
                {
                    "expiration_date": (
                        "La fecha de expiración no puede ser anterior "
                        "a la fecha de emisión."
                    )
                }
            )

    def __str__(self) -> str:
        return f"{self.name} — {self.issuer}"


class SidebarLink(OrderedVisibleModel):
    title = models.CharField(
        max_length=100,
        verbose_name="título",
    )

    description = models.CharField(
        max_length=220,
        blank=True,
        verbose_name="descripción",
    )

    url = models.CharField(
        max_length=500,
        verbose_name="ruta o URL",
        help_text=(
            "Puede ser una ruta como /dashboard o una URL completa "
            "como https://app.dominio.com."
        ),
    )

    icon_name = models.CharField(
        max_length=80,
        blank=True,
        verbose_name="icono",
    )

    badge_text = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="etiqueta",
        help_text="Ejemplo: Nuevo, Beta o Próximamente.",
    )

    open_in_new_tab = models.BooleanField(
        default=False,
        verbose_name="abrir en otra pestaña",
    )

    class Meta(OrderedVisibleModel.Meta):
        verbose_name = "enlace del sidebar"
        verbose_name_plural = "enlaces del sidebar"

    def __str__(self) -> str:
        return self.title


class ProfessionalStrength(OrderedVisibleModel):
    title = models.CharField(
        max_length=120,
        unique=True,
        verbose_name="fortaleza",
    )

    description = models.CharField(
        max_length=300,
        blank=True,
        verbose_name="descripción",
    )

    icon_name = models.CharField(
        max_length=80,
        blank=True,
        verbose_name="icono",
    )

    class Meta(OrderedVisibleModel.Meta):
        verbose_name = "fortaleza profesional"
        verbose_name_plural = "fortalezas profesionales"

    def __str__(self) -> str:
        return self.title

class SeoSettings(TimeStampedModel):
    site_title = models.CharField(
        max_length=180,
        default=(
            "Erick Manuel Rodríguez López | "
            "Software Engineer & Full-Stack Developer"
        ),
        verbose_name="título del sitio",
    )

    meta_description = models.CharField(
        max_length=320,
        default=(
            "Portfolio profesional de Erick Manuel Rodríguez López, "
            "Ingeniero de Software y desarrollador full-stack."
        ),
        verbose_name="descripción SEO",
    )

    keywords = models.CharField(
        max_length=500,
        blank=True,
        verbose_name="palabras clave",
    )

    canonical_url = models.URLField(
        blank=True,
        verbose_name="URL canónica",
    )

    og_image = models.ImageField(
        upload_to="seo/",
        blank=True,
        null=True,
        verbose_name="imagen para compartir",
    )

    robots_index = models.BooleanField(
        default=True,
        verbose_name="permitir indexación",
    )

    class Meta:
        verbose_name = "configuración SEO"
        verbose_name_plural = "configuración SEO"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return None

    def __str__(self) -> str:
        return self.site_title