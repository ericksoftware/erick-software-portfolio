import { useState } from 'react'
import {
  ArrowUpRight,
  Building2,
  ChevronDown,
} from 'lucide-react'
import { motion } from 'motion/react'

import type {
  Experience,
  SectionSettings,
} from '../types/portfolio.types'

interface ExperienceSectionProps {
  section?: SectionSettings
  experiences: Experience[]
}

const EXPERIENCES_PER_PAGE = 3

export function ExperienceSection({
  section,
  experiences,
}: ExperienceSectionProps) {
  const [visibleExperienceCount, setVisibleExperienceCount] =
    useState(EXPERIENCES_PER_PAGE)

  const visibleExperiences = experiences.slice(
    0,
    visibleExperienceCount,
  )

  const hasMoreExperiences =
    visibleExperienceCount < experiences.length

  function handleShowMoreExperiences(): void {
    setVisibleExperienceCount((currentCount) => (
      Math.min(
        currentCount + EXPERIENCES_PER_PAGE,
        experiences.length,
      )
    ))
  }

  return (
    <section
      id="experience"
      className="portfolio-section portfolio-experience"
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
          {section?.eyebrow || 'Experiencia'}
        </p>

        <h2>
          {section?.title
            || 'Experiencia construyendo software para proyectos reales'}
        </h2>

        {section?.description && (
          <p>{section.description}</p>
        )}
      </motion.div>

      {experiences.length > 0 ? (
        <>
          <div className="portfolio-experience-list">
            {visibleExperiences.map(
              (experience, index) => (
                <motion.article
                  key={experience.id}
                  className="portfolio-experience-item"
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
                    amount: 0.2,
                  }}
                  transition={{
                    duration: 0.45,
                    delay: index * 0.06,
                    ease: [0.22, 1, 0.36, 1],
                  }}
                >
                  <div className="portfolio-experience-item__marker">
                    <span />

                    {index
                      < visibleExperiences.length - 1 && (
                        <i aria-hidden="true" />
                      )}
                  </div>

                  <div className="portfolio-experience-item__content">
                    <header className="portfolio-experience-item__header">
                      <div>
                        <span className="portfolio-experience-item__period">
                          {experience.period_label}
                        </span>

                        <h3>{experience.role}</h3>

                        <p>
                          <Building2
                            size={16}
                            aria-hidden="true"
                          />

                          {experience.company}
                        </p>
                      </div>

                      {experience.company_url && (
                        <a
                          href={experience.company_url}
                          target="_blank"
                          rel="noreferrer"
                          aria-label={
                            `Visitar sitio de ${experience.company}`
                          }
                        >
                          <ArrowUpRight
                            size={18}
                            aria-hidden="true"
                          />
                        </a>
                      )}
                    </header>

                    <p className="portfolio-experience-item__summary">
                      {experience.summary}
                    </p>

                    {experience.impact && (
                      <div className="portfolio-experience-item__impact">
                        <strong>Impacto</strong>

                        <p>{experience.impact}</p>
                      </div>
                    )}

                    {experience.technologies.length > 0 && (
                      <div className="portfolio-experience-item__technologies">
                        {experience.technologies.map(
                          (technology) => (
                            <span key={technology.id}>
                              {technology.name}
                            </span>
                          ),
                        )}
                      </div>
                    )}
                  </div>
                </motion.article>
              ),
            )}
          </div>

          {hasMoreExperiences && (
            <div className="portfolio-experience-more">
              <button
                type="button"
                className="portfolio-button portfolio-button--secondary"
                onClick={handleShowMoreExperiences}
              >
                Ver más experiencia

                <ChevronDown
                  size={18}
                  aria-hidden="true"
                />
              </button>

              <span>
                Mostrando {visibleExperiences.length} de{' '}
                {experiences.length}
              </span>
            </div>
          )}
        </>
      ) : (
        <div className="portfolio-section-empty">
          Todavía no hay experiencia pública.
        </div>
      )}
    </section>
  )
}