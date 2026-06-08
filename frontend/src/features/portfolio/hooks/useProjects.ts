import { useEffect, useState } from 'react'

import { portfolioApi } from '../api/portfolioApi'
import type {
  Project,
} from '../types/portfolio.types'

interface UseProjectsResult {
  projects: Project[]
  isLoading: boolean
  error: Error | null
}

export function useProjects(): UseProjectsResult {
  const [projects, setProjects] = useState<Project[]>([])
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState<Error | null>(null)

  useEffect(() => {
    const controller = new AbortController()

    async function loadProjects(): Promise<void> {
      try {
        setIsLoading(true)
        setError(null)

        const result = await portfolioApi.getProjects(
          controller.signal,
        )

        setProjects(result)
      } catch (requestError) {
        if (controller.signal.aborted) {
          return
        }

        setError(
          requestError instanceof Error
            ? requestError
            : new Error(
                'No fue posible cargar los proyectos.',
              ),
        )
      } finally {
        if (!controller.signal.aborted) {
          setIsLoading(false)
        }
      }
    }

    void loadProjects()

    return () => {
      controller.abort()
    }
  }, [])

  return {
    projects,
    isLoading,
    error,
  }
}