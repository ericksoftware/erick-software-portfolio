import {
  Check,
  Code2,
} from 'lucide-react'
import { motion } from 'motion/react'

import type {
  ProfessionalStrength,
  SectionSettings,
  TechnologyCategory,
} from '../types/portfolio.types'
import { getPortfolioIcon } from './iconRegistry'

interface TechnologySectionProps {
  section?: SectionSettings
  categories: TechnologyCategory[]
  strengths: ProfessionalStrength[]
}

export function TechnologySection({
  section,
  categories,
  strengths,
}: TechnologySectionProps) {
  return (
    <section
      id="stack"
      className="portfolio-section portfolio-stack"
    >
      <motion.div
        className="portfolio-section__heading"
        initial={{
          opacity: 0,
          y: 20,
        }}
        whileInView={{
          opacity: 1,
          y: 0,
        }}
        viewport={{
          once: true,
          amount: 0.25,
        }}
        transition={{
          duration: 0.5,
          ease: [0.22, 1, 0.36, 1],
        }}
      >
        <p className="portfolio-eyebrow">
          {section?.eyebrow || 'Stack tecnológico'}
        </p>

        <h2>
          {section?.title
            || 'Tecnologías para construir productos modernos'}
        </h2>

        {section?.description && (
          <p>{section.description}</p>
        )}
      </motion.div>

      {categories.length > 0 ? (
        <div className="portfolio-stack-grid">
          {categories.map((category, index) => {
            const Icon = category.icon_name
              ? getPortfolioIcon(category.icon_name)
              : Code2

            return (
              <motion.article
                key={category.id}
                className="portfolio-stack-card"
                initial={{
                  opacity: 0,
                  y: 20,
                }}
                whileInView={{
                  opacity: 1,
                  y: 0,
                }}
                viewport={{
                  once: true,
                  amount: 0.15,
                }}
                transition={{
                  duration: 0.45,
                  delay: index * 0.05,
                  ease: [0.22, 1, 0.36, 1],
                }}
              >
                <header className="portfolio-stack-card__header">
                  <span className="portfolio-stack-card__icon">
                    <Icon
                      size={20}
                      aria-hidden="true"
                    />
                  </span>

                  <div>
                    <h3>{category.name}</h3>

                    {category.description && (
                      <p>{category.description}</p>
                    )}
                  </div>
                </header>

                <div className="portfolio-stack-card__technologies">
                  {category.technologies.map(
                    (technology) => (
                      <span key={technology.id}>
                        {technology.is_featured && (
                          <Check
                            size={13}
                            aria-hidden="true"
                          />
                        )}

                        {technology.name}
                      </span>
                    ),
                  )}
                </div>
              </motion.article>
            )
          })}
        </div>
      ) : (
        <div className="portfolio-section-empty">
          Todavía no hay tecnologías públicas.
        </div>
      )}

      {strengths.length > 0 && (
        <div className="portfolio-strengths">
          <div className="portfolio-strengths__heading">
            <p className="portfolio-eyebrow">
              Fortalezas profesionales
            </p>

            <h3>
              Habilidades que complementan el desarrollo técnico
            </h3>
          </div>

          <div className="portfolio-strengths__list">
            {strengths.map((strength) => (
              <article
                key={strength.id}
                className="portfolio-strength"
              >
                <span aria-hidden="true">
                  <Check size={14} />
                </span>

                <div>
                  <strong>{strength.title}</strong>

                  {strength.description && (
                    <p>{strength.description}</p>
                  )}
                </div>
              </article>
            ))}
          </div>
        </div>
      )}
    </section>
  )
}