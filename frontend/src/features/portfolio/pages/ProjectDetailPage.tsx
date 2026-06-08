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

import { portfolioApi } from '../api/portfolioApi'
import type {
  ProjectDetail,
} from '../types/portfolio.types'
import { AppError } from '../../../shared/components/AppError'
import { AppLoader } from '../../../shared/components/AppLoader'

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

  return (
    <main className="project-detail">
      <Link
        to="/"
        className="back-link"
      >
        <ArrowLeft
          size={18}
          aria-hidden="true"
        />

        Volver al portfolio
      </Link>

      <header className="project-detail__header">
        <span className="project-status">
          {project.status_label}
        </span>

        <h1>{project.title}</h1>

        <p>{project.short_description}</p>

        <div className="project-detail__actions">
          {project.demo_url && (
            <a
              href={project.demo_url}
              target="_blank"
              rel="noreferrer"
              className="button button--primary"
            >
              <ExternalLink
                size={18}
                aria-hidden="true"
              />

              Ver demostración
            </a>
          )}

          {project.repository_url
            && !project.is_repository_private && (
              <a
                href={project.repository_url}
                target="_blank"
                rel="noreferrer"
                className="button button--secondary"
              >
                <FaGithub
                    size={18}
                    aria-hidden="true"
                    />

                GitHub
              </a>
            )}
        </div>
      </header>

      <section className="project-detail__body">
        <div>
          <p className="eyebrow">
            Descripción
          </p>

          <h2>Acerca del proyecto</h2>

          <p>{project.description}</p>
        </div>

        {project.impact && (
          <div>
            <p className="eyebrow">
              Participación
            </p>

            <h2>Impacto y resultados</h2>

            <p>{project.impact}</p>
          </div>
        )}

        <div>
          <p className="eyebrow">
            Tecnologías
          </p>

          <div className="strength-list">
            {project.technologies.map(
              (technology) => (
                <span key={technology.id}>
                  {technology.name}
                </span>
              ),
            )}
          </div>
        </div>
      </section>
    </main>
  )
}