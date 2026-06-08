import {
  MoveUpRight,
} from 'lucide-react'

import type {
  SectionSettings,
  SiteProfile,
} from '../types/portfolio.types'

interface PortfolioHeaderProps {
  profile: SiteProfile
  sections: SectionSettings[]
}

const navigationKeys = new Set([
  'about',
  'stack',
  'experience',
  'projects',
  'contact',
])

export function PortfolioHeader({
  profile,
  sections,
}: PortfolioHeaderProps) {
  const navigationSections = sections.filter(
    (section) => navigationKeys.has(section.key),
  )

  return (
    <header className="portfolio-header">
      <div className="portfolio-header__inner">
        <a
          href="#top"
          className="portfolio-header__identity"
        >
          <span className="portfolio-header__monogram">
            ER
          </span>

          <span>
            <strong>
              {profile.full_name.split(' ')[0]}
            </strong>

            <small>
              Software Engineer
            </small>
          </span>
        </a>

        <nav
          className="portfolio-header__navigation"
          aria-label="Navegación principal"
        >
          {navigationSections.map((section) => (
            <a
              key={section.key}
              href={`#${section.key}`}
            >
              {section.navigation_label}
            </a>
          ))}
        </nav>

        <a
          href="#contact"
          className="portfolio-header__contact"
        >
          Contactar

          <MoveUpRight
            size={16}
            aria-hidden="true"
          />
        </a>
      </div>
    </header>
  )
}