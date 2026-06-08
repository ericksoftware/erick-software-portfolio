from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.text import slugify

from apps.portfolio.models import (
    Education,
    Experience,
    ProfessionalStrength,
    Project,
    SectionSettings,
    SidebarLink,
    SiteProfile,
    Technology,
    TechnologyCategory,
)


class Command(BaseCommand):
    help = (
        "Crea el contenido inicial del portfolio sin sobrescribir "
        "los registros existentes."
    )

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write("Cargando contenido inicial del portfolio...")

        self.create_profile()
        categories = self.create_technology_categories()
        technologies = self.create_technologies(categories)
        self.create_strengths()
        self.create_experiences(technologies)
        self.create_projects(technologies)
        self.create_education()
        self.create_sections()
        self.create_sidebar_links()

        self.stdout.write(
            self.style.SUCCESS(
                "Contenido inicial cargado correctamente."
            )
        )

    def get_or_create_message(
        self,
        model,
        lookup,
        defaults=None,
        label=None,
    ):
        instance, created = model.objects.get_or_create(
            **lookup,
            defaults=defaults or {},
        )

        display_name = label or str(instance)

        if created:
            self.stdout.write(
                self.style.SUCCESS(f"  Creado: {display_name}")
            )
        else:
            self.stdout.write(f"  Ya existe: {display_name}")

        return instance

    def create_profile(self):
        self.stdout.write("\nPerfil profesional")

        self.get_or_create_message(
            SiteProfile,
            {"pk": 1},
            {
                "full_name": "Erick Manuel Rodríguez López",
                "professional_title": (
                    "Software Engineer / Full-Stack Developer"
                ),
                "hero_eyebrow": "Ingeniero de Software",
                "hero_summary": (
                    "Construyo aplicaciones web modernas, escalables y "
                    "orientadas a resolver problemas reales, combinando "
                    "desarrollo full-stack, calidad de software y "
                    "aprendizaje continuo."
                ),
                "about_text": (
                    "Soy Ingeniero de Software graduado de la UABC, con "
                    "experiencia en desarrollo full-stack, QA/testing y "
                    "construcción de aplicaciones web modernas. He trabajado "
                    "con distintos lenguajes, frameworks y bases de datos, "
                    "adaptándome a las necesidades técnicas de cada proyecto."
                ),
                "work_philosophy": (
                    "Busco construir software mantenible, claro y útil. "
                    "Valoro la comunicación, las buenas prácticas, el trabajo "
                    "en equipo y la mejora continua."
                ),
                "technology_interests": (
                    "Arquitectura de software, aplicaciones web modernas, "
                    "APIs, experiencia de usuario, automatización, "
                    "infraestructura y productos digitales escalables."
                ),
                "location": "Tijuana, Baja California, México",
                "availability_text": (
                    "Disponible para nuevas oportunidades profesionales"
                ),
                "contact_cta_title": (
                    "Construyamos productos útiles y bien diseñados"
                ),
                "contact_cta_text": (
                    "Estoy abierto a oportunidades donde pueda aportar "
                    "experiencia, seguir creciendo y colaborar en productos "
                    "de software de calidad."
                ),
            },
            "Perfil principal",
        )

    def create_technology_categories(self):
        self.stdout.write("\nCategorías tecnológicas")

        category_data = [
            {
                "name": "Frontend",
                "slug": "frontend",
                "description": (
                    "Tecnologías para crear interfaces web modernas."
                ),
                "icon_name": "layout",
                "order": 1,
            },
            {
                "name": "Backend",
                "slug": "backend",
                "description": (
                    "Lenguajes y frameworks para servicios y aplicaciones."
                ),
                "icon_name": "server",
                "order": 2,
            },
            {
                "name": "Bases de datos",
                "slug": "databases",
                "description": (
                    "Motores relacionales y bases de datos documentales."
                ),
                "icon_name": "database",
                "order": 3,
            },
            {
                "name": "Dev tools",
                "slug": "dev-tools",
                "description": (
                    "Herramientas utilizadas durante el desarrollo."
                ),
                "icon_name": "terminal",
                "order": 4,
            },
            {
                "name": "Colaboración",
                "slug": "collaboration",
                "description": (
                    "Herramientas de coordinación y trabajo en equipo."
                ),
                "icon_name": "users",
                "order": 5,
            },
            {
                "name": "Metodologías y calidad",
                "slug": "methodologies-quality",
                "description": (
                    "Prácticas de organización, pruebas y calidad."
                ),
                "icon_name": "workflow",
                "order": 6,
            },
        ]

        categories = {}

        for data in category_data:
            slug = data["slug"]

            category = self.get_or_create_message(
                TechnologyCategory,
                {"slug": slug},
                {
                    "name": data["name"],
                    "description": data["description"],
                    "icon_name": data["icon_name"],
                    "order": data["order"],
                    "is_visible": True,
                },
                data["name"],
            )

            categories[slug] = category

        return categories

    def create_technologies(self, categories):
        self.stdout.write("\nTecnologías")

        technology_data = {
            "frontend": [
                "HTML",
                "CSS",
                "JavaScript",
                "TypeScript",
                "React",
                "Angular",
                "Bootstrap",
                "Tailwind CSS",
            ],
            "backend": [
                "Python",
                "Java",
                "PHP",
                "Django",
                "Spring Boot",
                "Flask",
                "REST APIs",
            ],
            "databases": [
                "MongoDB",
                "MySQL",
                "PostgreSQL",
                "MariaDB",
            ],
            "dev-tools": [
                "Git",
                "GitHub",
                "Linux",
            ],
            "collaboration": [
                "Jira",
                "Trello",
                "Asana",
                "Slack",
            ],
            "methodologies-quality": [
                "Scrum",
                "QA / Testing",
            ],
        }

        featured = {
            "React",
            "Python",
            "Java",
            "Django",
            "Spring Boot",
            "PostgreSQL",
        }

        icon_names = {
            "HTML": "html5",
            "CSS": "css3",
            "JavaScript": "javascript",
            "TypeScript": "typescript",
            "React": "react",
            "Angular": "angular",
            "Bootstrap": "bootstrap",
            "Tailwind CSS": "tailwindcss",
            "Python": "python",
            "Java": "java",
            "PHP": "php",
            "Django": "django",
            "Spring Boot": "spring",
            "Flask": "flask",
            "REST APIs": "api",
            "MongoDB": "mongodb",
            "MySQL": "mysql",
            "PostgreSQL": "postgresql",
            "MariaDB": "mariadb",
            "Git": "git",
            "GitHub": "github",
            "Linux": "linux",
            "Jira": "jira",
            "Trello": "trello",
            "Asana": "asana",
            "Slack": "slack",
            "Scrum": "workflow",
            "QA / Testing": "test-tube",
        }

        technologies = {}

        for category_slug, names in technology_data.items():
            category = categories[category_slug]

            for index, name in enumerate(names, start=1):
                slug = slugify(name.replace("/", " "))

                technology = self.get_or_create_message(
                    Technology,
                    {
                        "category": category,
                        "slug": slug,
                    },
                    {
                        "name": name,
                        "icon_name": icon_names.get(name, "code"),
                        "is_featured": name in featured,
                        "order": index,
                        "is_visible": True,
                    },
                    name,
                )

                technologies[name] = technology

        return technologies

    def create_strengths(self):
        self.stdout.write("\nFortalezas profesionales")

        strengths = [
            {
                "title": "Inglés C1",
                "description": (
                    "Competencia avanzada para comunicación profesional "
                    "y documentación técnica."
                ),
                "icon_name": "languages",
            },
            {
                "title": "Pensamiento lógico",
                "description": (
                    "Análisis estructurado de problemas y requerimientos."
                ),
                "icon_name": "brain",
            },
            {
                "title": "Resolución de problemas",
                "description": (
                    "Búsqueda de soluciones prácticas, mantenibles y claras."
                ),
                "icon_name": "lightbulb",
            },
            {
                "title": "Adaptabilidad",
                "description": (
                    "Capacidad para aprender tecnologías y procesos nuevos."
                ),
                "icon_name": "refresh-cw",
            },
            {
                "title": "Trabajo en equipo",
                "description": (
                    "Colaboración y comunicación dentro de equipos técnicos."
                ),
                "icon_name": "users",
            },
            {
                "title": "Aprendizaje continuo",
                "description": (
                    "Interés constante por mejorar conocimientos y prácticas."
                ),
                "icon_name": "book-open",
            },
        ]

        for index, data in enumerate(strengths, start=1):
            self.get_or_create_message(
                ProfessionalStrength,
                {"title": data["title"]},
                {
                    "description": data["description"],
                    "icon_name": data["icon_name"],
                    "order": index,
                    "is_visible": True,
                },
                data["title"],
            )

    def create_experiences(self, technologies):
        self.stdout.write("\nExperiencia")

        experience_data = [
            {
                "role": "Full Stack Developer Jr",
                "company": "Codifika Technologies S.A. de C.V.",
                "summary": (
                    "Participación en el desarrollo y mantenimiento de "
                    "aplicaciones web full-stack utilizando diferentes "
                    "frameworks, APIs y bases de datos."
                ),
                "impact": (
                    "Colaboración en soluciones empresariales, integración "
                    "de funcionalidades y mejora continua de aplicaciones."
                ),
                "technology_names": [
                    "Angular",
                    "Spring Boot",
                    "Django",
                    "Python",
                    "Java",
                    "MongoDB",
                    "MySQL",
                    "REST APIs",
                    "React",
                    "Linux",
                ],
                "order": 1,
            },
            {
                "role": "Full Stack React Developer",
                "company": "FCITEC UABC",
                "summary": (
                    "Desarrollo de una aplicación web utilizando React, "
                    "Flask y MongoDB, con una interfaz moderna construida "
                    "con Tailwind CSS."
                ),
                "impact": (
                    "Construcción de funcionalidades frontend y backend "
                    "para una plataforma web accesible desde internet."
                ),
                "technology_names": [
                    "HTML",
                    "Tailwind CSS",
                    "JavaScript",
                    "React",
                    "Flask",
                    "Python",
                    "MongoDB",
                ],
                "order": 2,
            },
            {
                "role": "Software Engineering",
                "company": "CISALUD UABC",
                "summary": (
                    "Participación en el desarrollo de una plataforma web "
                    "con tecnologías frontend, PHP y base de datos SQL."
                ),
                "impact": (
                    "Implementación y mantenimiento de funcionalidades "
                    "orientadas a las necesidades del proyecto."
                ),
                "technology_names": [
                    "HTML",
                    "CSS",
                    "JavaScript",
                    "PHP",
                    "MySQL",
                ],
                "order": 3,
            },
        ]

        for data in experience_data:
            experience = self.get_or_create_message(
                Experience,
                {
                    "role": data["role"],
                    "company": data["company"],
                },
                {
                    "summary": data["summary"],
                    "impact": data["impact"],
                    "order": data["order"],
                    "is_visible": True,
                },
                f"{data['role']} — {data['company']}",
            )

            if not experience.technologies.exists():
                experience.technologies.set(
                    [
                        technologies[name]
                        for name in data["technology_names"]
                        if name in technologies
                    ]
                )

    def create_projects(self, technologies):
        self.stdout.write("\nProyectos")

        project_data = [
            {
                "title": "DentixPro",
                "slug": "dentixpro",
                "short_description": (
                    "Aplicación web desarrollada con React, Flask "
                    "y MongoDB."
                ),
                "description": (
                    "Plataforma web construida como proyecto full-stack, "
                    "integrando una interfaz moderna, servicios backend "
                    "y persistencia de datos."
                ),
                "role": "Full Stack React Developer",
                "impact": (
                    "Participación en la construcción integral de la "
                    "aplicación y publicación de una versión funcional."
                ),
                "status": Project.Status.ACTIVE,
                "demo_url": "https://dentixpro.onrender.com/",
                "project_url": "https://dentixpro.onrender.com/",
                "is_featured": True,
                "technology_names": [
                    "HTML",
                    "Tailwind CSS",
                    "JavaScript",
                    "React",
                    "Flask",
                    "Python",
                    "MongoDB",
                ],
                "order": 1,
            },
            {
                "title": "CIMED",
                "slug": "cimed",
                "short_description": (
                    "Plataforma web desarrollada para CISALUD UABC."
                ),
                "description": (
                    "Proyecto web desarrollado con HTML, CSS, JavaScript, "
                    "PHP y una base de datos SQL."
                ),
                "role": "Software Engineering",
                "impact": (
                    "Participación en el desarrollo y mantenimiento de "
                    "funcionalidades para una plataforma institucional."
                ),
                "status": Project.Status.ACTIVE,
                "demo_url": "https://citecuvp.tij.uabc.mx/cimed/",
                "project_url": "https://citecuvp.tij.uabc.mx/cimed/",
                "is_featured": True,
                "technology_names": [
                    "HTML",
                    "CSS",
                    "JavaScript",
                    "PHP",
                    "MySQL",
                ],
                "order": 2,
            },
        ]

        for data in project_data:
            project = self.get_or_create_message(
                Project,
                {"slug": data["slug"]},
                {
                    "title": data["title"],
                    "short_description": data["short_description"],
                    "description": data["description"],
                    "role": data["role"],
                    "impact": data["impact"],
                    "status": data["status"],
                    "demo_url": data["demo_url"],
                    "project_url": data["project_url"],
                    "is_featured": data["is_featured"],
                    "order": data["order"],
                    "is_visible": True,
                },
                data["title"],
            )

            if not project.technologies.exists():
                project.technologies.set(
                    [
                        technologies[name]
                        for name in data["technology_names"]
                        if name in technologies
                    ]
                )

    def create_education(self):
        self.stdout.write("\nEducación")

        education_data = [
            {
                "institution": (
                    "Universidad Autónoma de Baja California"
                ),
                "program": "Ingeniería en Software",
                "location": "Tijuana, Baja California, México",
                "description": (
                    "Formación profesional en análisis, diseño, desarrollo "
                    "y mantenimiento de sistemas de software."
                ),
                "order": 1,
            },
            {
                "institution": (
                    "San Diego Global Knowledge University"
                ),
                "program": "Full-Stack Developer",
                "description": (
                    "Formación enfocada en desarrollo de aplicaciones web "
                    "y tecnologías full-stack."
                ),
                "order": 2,
            },
        ]

        for data in education_data:
            self.get_or_create_message(
                Education,
                {
                    "institution": data["institution"],
                    "program": data["program"],
                },
                {
                    "location": data.get("location", ""),
                    "description": data["description"],
                    "order": data["order"],
                    "is_visible": True,
                },
                f"{data['program']} — {data['institution']}",
            )

    def create_sections(self):
        self.stdout.write("\nSecciones")

        sections = [
            {
                "key": "hero",
                "navigation_label": "Inicio",
                "eyebrow": "Software Engineer",
                "title": (
                    "Ingeniería de software con enfoque en productos reales"
                ),
                "description": (
                    "Desarrollo soluciones web modernas, escalables y "
                    "centradas en las necesidades de usuarios y empresas."
                ),
                "order": 1,
            },
            {
                "key": "about",
                "navigation_label": "Sobre mí",
                "eyebrow": "Perfil profesional",
                "title": (
                    "Tecnología, criterio y aprendizaje continuo"
                ),
                "description": (
                    "Una visión profesional basada en la calidad, la "
                    "adaptabilidad y la resolución de problemas."
                ),
                "order": 2,
            },
            {
                "key": "stack",
                "navigation_label": "Tecnologías",
                "eyebrow": "Stack tecnológico",
                "title": (
                    "Herramientas para construir productos modernos"
                ),
                "description": (
                    "Experiencia en frontend, backend, bases de datos "
                    "y herramientas de desarrollo."
                ),
                "order": 3,
            },
            {
                "key": "experience",
                "navigation_label": "Experiencia",
                "eyebrow": "Trayectoria",
                "title": (
                    "Experiencia práctica en desarrollo de software"
                ),
                "description": (
                    "Participación en productos profesionales, "
                    "universitarios e institucionales."
                ),
                "order": 4,
            },
            {
                "key": "projects",
                "navigation_label": "Proyectos",
                "eyebrow": "Trabajo destacado",
                "title": (
                    "Proyectos construidos para necesidades reales"
                ),
                "description": (
                    "Una selección de plataformas y aplicaciones "
                    "en las que he participado."
                ),
                "order": 5,
            },
            {
                "key": "education",
                "navigation_label": "Educación",
                "eyebrow": "Formación",
                "title": "Educación y preparación profesional",
                "description": (
                    "Formación académica y aprendizaje técnico continuo."
                ),
                "order": 6,
            },
            {
                "key": "contact",
                "navigation_label": "Contacto",
                "eyebrow": "Conversemos",
                "title": (
                    "¿Tienes una oportunidad o proyecto en mente?"
                ),
                "description": (
                    "Estoy abierto a conversar sobre oportunidades "
                    "profesionales y proyectos tecnológicos."
                ),
                "order": 7,
            },
        ]

        for data in sections:
            key = data["key"]

            self.get_or_create_message(
                SectionSettings,
                {"key": key},
                {
                    "navigation_label": data["navigation_label"],
                    "eyebrow": data["eyebrow"],
                    "title": data["title"],
                    "description": data["description"],
                    "order": data["order"],
                    "is_visible": True,
                },
                data["navigation_label"],
            )

    def create_sidebar_links(self):
        self.stdout.write("\nSidebar")

        links = [
            {
                "title": "Portfolio",
                "description": "Página profesional principal.",
                "url": "/portfolio",
                "icon_name": "user-round",
                "order": 1,
            },
            {
                "title": "Music Platform",
                "description": "Plataforma musical.",
                "url": "/music-platform",
                "icon_name": "music",
                "order": 2,
            },
            {
                "title": "Dashboard",
                "description": "Paneles y visualización de información.",
                "url": "/dashboard",
                "icon_name": "layout-dashboard",
                "order": 3,
            },
            {
                "title": "AI Projects",
                "description": "Proyectos relacionados con inteligencia artificial.",
                "url": "/ai-projects",
                "icon_name": "sparkles",
                "order": 4,
            },
            {
                "title": "Tools",
                "description": "Herramientas y utilidades.",
                "url": "/tools",
                "icon_name": "wrench",
                "order": 5,
            },
            {
                "title": "Apps",
                "description": "Aplicaciones publicadas.",
                "url": "/apps",
                "icon_name": "blocks",
                "order": 6,
            },
        ]

        for data in links:
            self.get_or_create_message(
                SidebarLink,
                {
                    "title": data["title"],
                },
                {
                    "description": data["description"],
                    "url": data["url"],
                    "icon_name": data["icon_name"],
                    "order": data["order"],
                    # Permanecerán ocultos hasta que las rutas existan.
                    "is_visible": False,
                },
                data["title"],
            )