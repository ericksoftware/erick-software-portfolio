import {
  ArrowUpRight,
  Mail,
  MapPin,
} from 'lucide-react'
import {
  FaGithub,
  FaLinkedinIn,
} from 'react-icons/fa'

import type {
  SectionSettings,
  SiteProfile,
  SocialLink,
} from '../types/portfolio.types'

interface ContactSectionProps {
  profile: SiteProfile
  section?: SectionSettings
  socialLinks: SocialLink[]
}

export function ContactSection({
  profile,
  section,
  socialLinks,
}: ContactSectionProps) {
  const github = socialLinks.find(
    (link) => link.platform === 'github',
  )

  const linkedin = socialLinks.find(
    (link) => link.platform === 'linkedin',
  )

  const emailLink = socialLinks.find(
    (link) => link.platform === 'email',
  )

  const emailUrl =
    emailLink?.url
    || (
      profile.contact_email
        ? `mailto:${profile.contact_email}`
        : ''
    )

  return (
    <section
      id="contact"
      className="portfolio-contact-section"
    >
      <div className="portfolio-section__heading">
        <p className="portfolio-eyebrow">
          {section?.eyebrow || 'Contacto'}
        </p>

        <h2>
          {section?.title
            || profile.contact_cta_title
            || 'Conversemos sobre tu próxima oportunidad'}
        </h2>

        <p>
          {section?.description
            || profile.contact_cta_text}
        </p>
      </div>

      <div className="portfolio-contact-grid">
        <article className="portfolio-contact-card portfolio-contact-card--primary">
          <div className="portfolio-contact-card__icon">
            <Mail
              size={22}
              aria-hidden="true"
            />
          </div>

          <div>
            <span>Correo electrónico</span>

            <strong>
              {profile.contact_email
                || 'Correo pendiente de configurar'}
            </strong>
          </div>

          {emailUrl && (
            <a
              href={emailUrl}
              aria-label="Enviar correo electrónico"
            >
              <ArrowUpRight
                size={19}
                aria-hidden="true"
              />
            </a>
          )}
        </article>

        <article className="portfolio-contact-card">
          <div className="portfolio-contact-card__icon">
            <MapPin
              size={22}
              aria-hidden="true"
            />
          </div>

          <div>
            <span>Ubicación</span>

            <strong>
              {profile.location}
            </strong>
          </div>
        </article>

        {linkedin && (
          <article className="portfolio-contact-card">
            <div className="portfolio-contact-card__icon">
              <FaLinkedinIn
                size={20}
                aria-hidden="true"
              />
            </div>

            <div>
              <span>Perfil profesional</span>

              <strong>LinkedIn</strong>
            </div>

            <a
              href={linkedin.url}
              target="_blank"
              rel="noreferrer"
              aria-label="Abrir LinkedIn"
            >
              <ArrowUpRight
                size={19}
                aria-hidden="true"
              />
            </a>
          </article>
        )}

        {github && (
          <article className="portfolio-contact-card">
            <div className="portfolio-contact-card__icon">
              <FaGithub
                size={20}
                aria-hidden="true"
              />
            </div>

            <div>
              <span>Código y proyectos</span>

              <strong>GitHub</strong>
            </div>

            <a
              href={github.url}
              target="_blank"
              rel="noreferrer"
              aria-label="Abrir GitHub"
            >
              <ArrowUpRight
                size={19}
                aria-hidden="true"
              />
            </a>
          </article>
        )}
      </div>

      <div className="portfolio-contact-availability">
        <span aria-hidden="true" />

        {profile.availability_text}
      </div>
    </section>
  )
}