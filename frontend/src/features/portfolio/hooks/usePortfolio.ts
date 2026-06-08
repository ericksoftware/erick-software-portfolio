import { useEffect, useState } from 'react'

import { portfolioApi } from '../api/portfolioApi'
import type { PortfolioData } from '../types/portfolio.types'

interface UsePortfolioResult {
  data: PortfolioData | null
  isLoading: boolean
  error: Error | null
}

export function usePortfolio(): UsePortfolioResult {
  const [data, setData] = useState<PortfolioData | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState<Error | null>(null)

  useEffect(() => {
    const controller = new AbortController()

    async function loadPortfolio(): Promise<void> {
      try {
        setIsLoading(true)
        setError(null)

        const portfolio = await portfolioApi.getPortfolio(
          controller.signal,
        )

        setData(portfolio)
      } catch (requestError) {
        if (controller.signal.aborted) {
          return
        }

        setError(
          requestError instanceof Error
            ? requestError
            : new Error(
                'No fue posible cargar el portfolio.',
              ),
        )
      } finally {
        if (!controller.signal.aborted) {
          setIsLoading(false)
        }
      }
    }

    void loadPortfolio()

    return () => {
      controller.abort()
    }
  }, [])

  return {
    data,
    isLoading,
    error,
  }
}