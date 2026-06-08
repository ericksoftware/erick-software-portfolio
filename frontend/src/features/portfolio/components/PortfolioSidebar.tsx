import {
  ExternalLink,
  Grid2X2,
  X,
} from 'lucide-react'

import type {
  SidebarLink,
} from '../types/portfolio.types'
import { getPortfolioIcon } from './iconRegistry'

interface PortfolioSidebarProps {
  links: SidebarLink[]
  isOpen: boolean
  onClose: () => void
}

export function PortfolioSidebar({
  links,
  isOpen,
  onClose,
}: PortfolioSidebarProps) {
  return (
    <>
      <button
        type="button"
        className={[
          'portfolio-sidebar__overlay',
          isOpen
            ? 'portfolio-sidebar__overlay--visible'
            : '',
        ].join(' ')}
        aria-label="Cerrar menú de aplicaciones"
        onClick={onClose}
      />

      <aside
        className={[
          'portfolio-sidebar',
          isOpen
            ? 'portfolio-sidebar--open'
            : '',
        ].join(' ')}
        aria-label="Otras aplicaciones y proyectos"
      >
        <div className="portfolio-sidebar__header">
          <a
            href="/"
            className="portfolio-sidebar__brand"
            aria-label="Inicio del portfolio"
          >
            <span>ER</span>

            <div>
              <strong>ErickSoftware</strong>
              <small>Software</small>
            </div>
          </a>

          <button
            type="button"
            className="portfolio-sidebar__close"
            aria-label="Cerrar menú"
            onClick={onClose}
          >
            <X
              size={19}
              aria-hidden="true"
            />
          </button>
        </div>

        <div className="portfolio-sidebar__label">
          <Grid2X2
            size={15}
            aria-hidden="true"
          />

          Ecosistema
        </div>

        <nav className="portfolio-sidebar__navigation">
          {links.length > 0 ? (
            links.map((link) => {
              const Icon = getPortfolioIcon(
                link.icon_name,
              )

              const isExternal =
                link.url.startsWith('http://')
                || link.url.startsWith('https://')

              return (
                <a
                  key={link.id}
                  href={link.url}
                  className="portfolio-sidebar__link"
                  target={
                    link.open_in_new_tab
                      ? '_blank'
                      : undefined
                  }
                  rel={
                    link.open_in_new_tab
                      ? 'noreferrer'
                      : undefined
                  }
                  onClick={onClose}
                >
                  <span className="portfolio-sidebar__icon">
                    <Icon
                      size={19}
                      aria-hidden="true"
                    />
                  </span>

                  <span className="portfolio-sidebar__link-content">
                    <strong>
                      {link.title}
                    </strong>

                    {link.description && (
                      <small>
                        {link.description}
                      </small>
                    )}
                  </span>

                  {link.badge_text ? (
                    <span className="portfolio-sidebar__badge">
                      {link.badge_text}
                    </span>
                  ) : (
                    isExternal && (
                      <ExternalLink
                        className="portfolio-sidebar__external"
                        size={15}
                        aria-hidden="true"
                      />
                    )
                  )}
                </a>
              )
            })
          ) : (
            <div className="portfolio-sidebar__empty">
              <Grid2X2
                size={24}
                aria-hidden="true"
              />

              <strong>Próximamente</strong>

              <p>
                Tus demás aplicaciones aparecerán aquí
                cuando las actives desde el panel.
              </p>
            </div>
          )}
        </nav>

        <footer className="portfolio-sidebar__footer">
          <span className="portfolio-sidebar__status-dot" />

          Sistemas disponibles
        </footer>
      </aside>
    </>
  )
}