import { useState } from 'react'
import {
  ArrowRight,
  BriefcaseBusiness,
  ChevronDown,
  Code2,
  ExternalLink,
  FolderKanban,
  GraduationCap,
} from 'lucide-react'
import { Link } from 'react-router'

import { AppError } from '../../../shared/components/AppError'
import { AppLoader } from '../../../shared/components/AppLoader'
import { ContactSection } from '../components/ContactSection'
import { ExperienceSection } from '../components/ExperienceSection'
import { HeroSection } from '../components/HeroSection'
import { PortfolioShell } from '../components/PortfolioShell'
import { TechnologySection } from '../components/TechnologySection'
import { usePortfolio } from '../hooks/usePortfolio'
import { useProjects } from '../hooks/useProjects'

const PROJECTS_PER_PAGE = 3

export function HomePage() {
  const [visibleProjectCount, setVisibleProjectCount] =
    useState(PROJECTS_PER_PAGE)

  const {
    data,
    isLoading,
    error,
  } = usePortfolio()

  const {
    projects,
    isLoading: projectsLoading,
    error: projectsError,
  } = useProjects()

  if (isLoading) {
    return <AppLoader />
  }

  if (error || !data || !data.profile) {
    return <AppError />
  }

  const technologyCount =
    data.technology_categories.reduce(
      (total, category) => (
        total + category.technologies.length
      ),
      0,
    )

  const heroSection = data.sections.find(
    (section) => section.key === 'hero',
  )

  const projectsSection = data.sections.find(
    (section) => section.key === 'projects',
  )

  const experienceSection = data.sections.find(
    (section) => section.key === 'experience',
  )

  const educationSection = data.sections.find(
    (section) => section.key === 'education',
  )

  const stackSection = data.sections.find(
    (section) => section.key === 'stack',
  )

  const aboutSection = data.sections.find(
    (section) => section.key === 'about',
  )

  const contactSection = data.sections.find(
    (section) => section.key === 'contact',
  )

  const visibleProjects = projects.slice(
    0,
    visibleProjectCount,
  )

  const hasMoreProjects =
    visibleProjectCount < projects.length

  function handleShowMoreProjects(): void {
    setVisibleProjectCount((currentCount) => (
      Math.min(
        currentCount + PROJECTS_PER_PAGE,
        projects.length,
      )
    ))
  }

  return (
    <PortfolioShell data={data}>
      {/* 1. HERO */}

      <HeroSection
        profile={data.profile}
        section={heroSection}
        socialLinks={data.social_links}
        technologyCount={technologyCount}
        projectCount={
          projectsLoading
            ? data.featured_projects.length
            : projects.length
        }
        experienceCount={data.experiences.length}
      />

      {/* 2. PROYECTOS */}

      <section
        id="projects"
        className="portfolio-section"
      >
        <div className="portfolio-section__heading">

          <h2>
            {projectsSection?.title || 'Proyectos'}
          </h2>

          {projectsSection?.description && (
            <p>{projectsSection.description}</p>
          )}
        </div>

        {projectsLoading && (
          <div className="portfolio-projects-state">
            Cargando proyectos...
          </div>
        )}

        {projectsError && !projectsLoading && (
          <div
            className="portfolio-projects-state portfolio-projects-state--error"
            role="alert"
          >
            No fue posible cargar los proyectos.
          </div>
        )}

        {!projectsLoading
          && !projectsError
          && projects.length === 0 && (
            <div className="portfolio-projects-state">
              Todavía no hay proyectos públicos.
            </div>
          )}

        {!projectsLoading
          && !projectsError
          && projects.length > 0 && (
            <>
              <div className="portfolio-project-grid">
                {visibleProjects.map((project) => (
                  <article
                    key={project.id}
                    className="portfolio-project-card"
                  >
                    <div className="portfolio-project-card__visual">
                      {project.cover_image_url ? (
                        <img
                          src={project.cover_image_url}
                          alt={`Vista previa de ${project.title}`}
                        />
                      ) : (
                        <div className="portfolio-project-card__fallback">
                          <span>
                            {project.title.slice(0, 2)}
                          </span>
                        </div>
                      )}

                      <span className="portfolio-project-card__status">
                        {project.status_label}
                      </span>
                    </div>

                    <div className="portfolio-project-card__content">
                      {project.role && (
                        <p>{project.role}</p>
                      )}

                      <h3>{project.title}</h3>

                      <span>
                        {project.short_description}
                      </span>

                      {project.technologies.length > 0 && (
                        <div className="portfolio-project-card__technologies">
                          {project.technologies
                            .slice(0, 4)
                            .map((technology) => (
                              <small key={technology.id}>
                                {technology.name}
                              </small>
                            ))}
                        </div>
                      )}

                      <Link
                        to={`/projects/${project.slug}`}
                        className="portfolio-project-card__link"
                      >
                        Explorar proyecto

                        <ArrowRight
                          size={17}
                          aria-hidden="true"
                        />
                      </Link>
                    </div>
                  </article>
                ))}
              </div>

              {hasMoreProjects && (
                <div className="portfolio-projects-more">
                  <button
                    type="button"
                    className="portfolio-button portfolio-button--secondary"
                    onClick={handleShowMoreProjects}
                  >
                    Ver más proyectos

                    <ChevronDown
                      size={18}
                      aria-hidden="true"
                    />
                  </button>

                  <span>
                    Mostrando {visibleProjects.length} de{' '}
                    {projects.length}
                  </span>
                </div>
              )}
            </>
          )}
      </section>

      {/* 3. EXPERIENCIA */}

      <ExperienceSection
        section={experienceSection}
        experiences={data.experiences}
      />

      {/* 4. EDUCACIÓN */}

      <section
        id="education"
        className="portfolio-section"
      >
        <div className="portfolio-section__heading">

          <h2>
            {educationSection?.title
              || 'Educación y preparación profesional'}
          </h2>

          {educationSection?.description && (
            <p>{educationSection.description}</p>
          )}
        </div>

        {data.education.length > 0 ? (
          <div className="portfolio-stack-grid">
            {data.education.map((education) => (
              <article
                key={education.id}
                className="portfolio-stack-card"
              >
                <header className="portfolio-stack-card__header">
                  <span className="portfolio-stack-card__icon">
                    {education.logo_url ? (
                      <img
                        src={education.logo_url}
                        alt={`Logotipo de ${education.institution}`}
                      />
                    ) : (
                      <GraduationCap
                        size={20}
                        aria-hidden="true"
                      />
                    )}
                  </span>

                  <div>
                    <h3>{education.program}</h3>

                    <p>{education.institution}</p>
                  </div>

                  {education.institution_url && (
                    <a
                      href={education.institution_url}
                      target="_blank"
                      rel="noreferrer"
                      aria-label={
                        `Visitar sitio de ${education.institution}`
                      }
                      className="portfolio-education-link"
                    >
                      <ExternalLink
                        size={17}
                        aria-hidden="true"
                      />
                    </a>
                  )}
                </header>

                {education.description && (
                  <p className="portfolio-education-description">
                    {education.description}
                  </p>
                )}

                <div className="portfolio-stack-card__technologies">
                  {education.period_label && (
                    <span>
                      {education.period_label}
                    </span>
                  )}

                  {education.location && (
                    <span>
                      {education.location}
                    </span>
                  )}
                </div>
              </article>
            ))}
          </div>
        ) : (
          <div className="portfolio-section-empty">
            Todavía no hay educación pública.
          </div>
        )}

        {data.certifications.length > 0 && (
          <div className="portfolio-certifications">
            <div className="portfolio-certifications__heading">

              <h3>Preparación técnica complementaria</h3>
            </div>

            <div className="portfolio-stack-grid">
              {data.certifications.map((certification) => (
                <article
                  key={certification.id}
                  className="portfolio-stack-card"
                >
                  <header className="portfolio-stack-card__header">
                    <span className="portfolio-stack-card__icon">
                      <GraduationCap
                        size={20}
                        aria-hidden="true"
                      />
                    </span>

                    <div>
                      <h3>{certification.name}</h3>

                      <p>{certification.issuer}</p>
                    </div>

                    {certification.credential_url && (
                      <a
                        href={certification.credential_url}
                        target="_blank"
                        rel="noreferrer"
                        aria-label={
                          `Abrir certificación ${certification.name}`
                        }
                        className="portfolio-education-link"
                      >
                        <ExternalLink
                          size={17}
                          aria-hidden="true"
                        />
                      </a>
                    )}
                  </header>

                  <div className="portfolio-stack-card__technologies">
                    {certification.issue_date && (
                      <span>
                        Emitida en{' '}
                        {new Date(
                          `${certification.issue_date}T00:00:00`,
                        ).getFullYear()}
                      </span>
                    )}

                    {certification.credential_id && (
                      <span>
                        ID: {certification.credential_id}
                      </span>
                    )}
                  </div>
                </article>
              ))}
            </div>
          </div>
        )}
      </section>

      {/* 5. STACK TECNOLÓGICO */}

      <TechnologySection
        section={stackSection}
        categories={data.technology_categories}
        strengths={data.strengths}
      />

      {/* 6. SOBRE MÍ */}

      <section
        id="about"
        className="portfolio-section"
      >
        <div className="portfolio-section__heading">

          <h2>
            {aboutSection?.title
              || 'Tecnología, criterio y aprendizaje continuo'}
          </h2>

          {aboutSection?.description && (
            <p>{aboutSection.description}</p>
          )}
        </div>

        <div className="portfolio-about-grid">
          <article className="portfolio-about-card portfolio-about-card--large">
            <Code2 aria-hidden="true" />

            <h3>Perfil profesional</h3>

            <p>{data.profile.about_text}</p>
          </article>

          <article className="portfolio-about-card">
            <BriefcaseBusiness aria-hidden="true" />

            <h3>Filosofía de trabajo</h3>

            <p>
              {data.profile.work_philosophy}
            </p>
          </article>

          <article className="portfolio-about-card">
            <FolderKanban aria-hidden="true" />

            <h3>Intereses tecnológicos</h3>

            <p>
              {data.profile.technology_interests}
            </p>
          </article>
        </div>
      </section>

      {/* 7. CONTACTO */}

      <ContactSection
        profile={data.profile}
        section={contactSection}
        socialLinks={data.social_links}
      />
    </PortfolioShell>
  )
}