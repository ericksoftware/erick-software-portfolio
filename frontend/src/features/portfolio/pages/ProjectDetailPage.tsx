import { useEffect, useState } from 'react'
import {
  ArrowLeft,
  ExternalLink,
} from 'lucide-react'
import { FaGithub } from 'react-icons/fa'
import {
  Link,
  useParams,
} from 'react-router'

import { AppError } from '../../../shared/components/AppError'
import { AppLoader } from '../../../shared/components/AppLoader'
import { portfolioApi } from '../api/portfolioApi'
import type {
  ProjectDetail,
} from '../types/portfolio.types'

function getProjectInitials(title: string): string {
  const words = title
    .trim()
    .split(/\s+/)
    .filter(Boolean)

  if (words.length === 0) {
    return 'PR'
  }

  if (words.length === 1) {
    return words[0].slice(0, 2).toUpperCase()
  }

  return `${words[0][0]}${words[1][0]}`.toUpperCase()
}

export function ProjectDetailPage() {
  const { slug } = useParams<{
    slug: string
  }>()

  const [project, setProject] =
    useState<ProjectDetail | null>(null)

  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState<Error | null>(null)

  useEffect(() => {
    const controller = new AbortController()

    async function loadProject(): Promise<void> {
      if (!slug) {
        setError(
          new Error('El proyecto solicitado no es válido.'),
        )

        setIsLoading(false)
        return
      }

      try {
        setIsLoading(true)
        setError(null)

        const result = await portfolioApi.getProjectBySlug(
          slug,
          controller.signal,
        )

        setProject(result)
      } catch (requestError) {
        if (controller.signal.aborted) {
          return
        }

        setError(
          requestError instanceof Error
            ? requestError
            : new Error(
                'No fue posible cargar el proyecto.',
              ),
        )
      } finally {
        if (!controller.signal.aborted) {
          setIsLoading(false)
        }
      }
    }

    void loadProject()

    return () => {
      controller.abort()
    }
  }, [slug])

  if (isLoading) {
    return <AppLoader />
  }

  if (error || !project) {
    return (
      <AppError
        title="Proyecto no disponible"
        message={
          'El proyecto no existe, está oculto '
          + 'o no pudo cargarse.'
        }
      />
    )
  }

  const primaryUrl =
    project.demo_url || project.project_url

  const hasGallery = project.gallery.some(
    (image) => Boolean(image.image_url),
  )

  return (
    <main className="project-detail">
      <header className="project-detail__topbar">
        <Link
          to="/"
          className="project-detail__back"
        >
          <ArrowLeft
            size={17}
            aria-hidden="true"
          />

          Volver al portfolio
        </Link>

        <span className="project-detail__status">
          {project.status_label}
        </span>
      </header>

      <section className="project-detail__hero">
        <div className="project-detail__intro">

          <h1>{project.title}</h1>

          <p className="project-detail__lead">
            {project.short_description}
          </p>

          <div className="project-detail__actions">
            {primaryUrl && (
              <a
                href={primaryUrl}
                target="_blank"
                rel="noreferrer"
                className="portfolio-button portfolio-button--primary"
              >
                Ver proyecto

                <ExternalLink
                  size={17}
                  aria-hidden="true"
                />
              </a>
            )}

            {project.repository_url
              && !project.is_repository_private && (
                <a
                  href={project.repository_url}
                  target="_blank"
                  rel="noreferrer"
                  className="portfolio-button portfolio-button--secondary"
                >
                  <FaGithub
                    size={17}
                    aria-hidden="true"
                  />

                  GitHub
                </a>
              )}
          </div>
        </div>

        <div className="project-detail__cover">
          {project.cover_image_url ? (
            <img
              src={project.cover_image_url}
              alt={`Vista previa de ${project.title}`}
            />
          ) : (
            <div className="project-detail__cover-fallback">
              {getProjectInitials(project.title)}
            </div>
          )}
        </div>
      </section>

      <section className="project-detail__content">
        <article className="project-detail__panel project-detail__panel--wide">

          <h2>Acerca del proyecto</h2>

          <p>{project.description}</p>
        </article>

        {project.impact && (
          <article className="project-detail__panel">

            <h2>Impacto y participación</h2>

            <p>{project.impact}</p>
          </article>
        )}

        {project.technologies.length > 0 && (
          <article className="project-detail__panel">

            <h2>Tecnologías utilizadas</h2>

            <div className="project-detail__technologies">
              {project.technologies.map(
                (technology) => (
                  <span key={technology.id}>
                    {technology.name}
                  </span>
                ),
              )}
            </div>
          </article>
        )}
      </section>

      {hasGallery && (
        <section className="project-detail__gallery-section">
          <div className="project-detail__section-heading">

            <h2>Vistas del proyecto</h2>
          </div>

          <div className="project-detail__gallery">
            {project.gallery.map((image) => {
              if (!image.image_url) {
                return null
              }

              return (
                <figure
                  key={image.id}
                  className="project-detail__gallery-item"
                >
                  <img
                    src={image.image_url}
                    alt={
                      image.alt_text
                      || `Imagen de ${project.title}`
                    }
                  />

                  {image.caption && (
                    <figcaption>
                      {image.caption}
                    </figcaption>
                  )}
                </figure>
              )
            })}
          </div>
        </section>
      )}
    </main>
  )
}