import { apiRequest } from '../../../shared/lib/apiClient'
import type {
  PortfolioData,
  Project,
  ProjectDetail,
} from '../types/portfolio.types'

export const portfolioApi = {
  getPortfolio(
    signal?: AbortSignal,
  ): Promise<PortfolioData> {
    return apiRequest<PortfolioData>(
      '/portfolio/',
      {
        signal,
      },
    )
  },

  getProjects(
    signal?: AbortSignal,
  ): Promise<Project[]> {
    return apiRequest<Project[]>(
      '/projects/',
      {
        signal,
      },
    )
  },

  getProjectBySlug(
    slug: string,
    signal?: AbortSignal,
  ): Promise<ProjectDetail> {
    return apiRequest<ProjectDetail>(
      `/projects/${encodeURIComponent(slug)}/`,
      {
        signal,
      },
    )
  },
}