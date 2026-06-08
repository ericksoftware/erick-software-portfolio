import type { PropsWithChildren } from 'react'

import type {
  PortfolioData,
} from '../types/portfolio.types'
import { PortfolioHeader } from './PortfolioHeader'

interface PortfolioShellProps extends PropsWithChildren {
  data: PortfolioData
}

export function PortfolioShell({
  data,
  children,
}: PortfolioShellProps) {
  if (!data.profile) {
    return null
  }

  return (
    <div className="portfolio-shell">
      <PortfolioHeader
        profile={data.profile}
        sections={data.sections}
      />

      <main className="portfolio-shell__main">
        {children}
      </main>
    </div>
  )
}