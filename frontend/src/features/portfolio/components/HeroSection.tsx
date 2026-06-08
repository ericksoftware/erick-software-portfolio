import {
  ArrowDown,
  ArrowRight,
  Mail,
  MapPin,
} from 'lucide-react'
import { motion } from 'motion/react'
import {
  FaGithub,
  FaLinkedinIn,
} from 'react-icons/fa'

import type {
  SectionSettings,
  SiteProfile,
  SocialLink,
} from '../types/portfolio.types'

interface HeroSectionProps {
  profile: SiteProfile
  section?: SectionSettings
  socialLinks: SocialLink[]
  technologyCount: number
  projectCount: number
  experienceCount: number
}

function getInitials(fullName: string): string {
  const words = fullName
    .trim()
    .split(/\s+/)
    .filter(Boolean)

  if (words.length === 0) {
    return 'ER'
  }

  if (words.length === 1) {
    return words[0].slice(0, 2).toUpperCase()
  }

  return `${words[0][0]}${words[1][0]}`.toUpperCase()
}

export function HeroSection({
  profile,
  section,
  socialLinks,
  technologyCount,
  projectCount,
  experienceCount,
}: HeroSectionProps) {
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
      id="top"
      className="portfolio-hero"
    >
      <div className="portfolio-hero__glow portfolio-hero__glow--one" />

      <div className="portfolio-hero__glow portfolio-hero__glow--two" />

      <div className="portfolio-hero__grid">
        <motion.div
          className="portfolio-hero__content"
          initial={{
            opacity: 0,
            y: 20,
          }}
          animate={{
            opacity: 1,
            y: 0,
          }}
          transition={{
            duration: 0.6,
            ease: [0.22, 1, 0.36, 1],
          }}
        >
          <div className="portfolio-hero__availability">
            <span aria-hidden="true" />

            {profile.availability_text}
          </div>

          <p className="portfolio-eyebrow">
            {section?.eyebrow || profile.hero_eyebrow}
          </p>

          <h1>
            {profile.full_name}
          </h1>

          <p className="portfolio-hero__profession">
            {profile.professional_title}
          </p>

          <p className="portfolio-hero__summary">
            {profile.hero_summary}
          </p>

          <div className="portfolio-hero__location">
            <MapPin
              size={17}
              aria-hidden="true"
            />

            {profile.location}
          </div>

          <div className="portfolio-hero__actions">
            <a
              href="#contact"
              className="portfolio-button portfolio-button--primary"
            >
              Contactar

              <ArrowRight
                size={18}
                aria-hidden="true"
              />
            </a>

            <a
              href="#projects"
              className="portfolio-button portfolio-button--secondary"
            >
              Ver proyectos

              <ArrowDown
                size={17}
                aria-hidden="true"
              />
            </a>
          </div>

          <div className="portfolio-hero__socials">
            {github && (
              <a
                href={github.url}
                target="_blank"
                rel="noreferrer"
                aria-label="Visitar GitHub"
              >
                <FaGithub
                  size={18}
                  aria-hidden="true"
                />

                GitHub
              </a>
            )}

            {linkedin && (
              <a
                href={linkedin.url}
                target="_blank"
                rel="noreferrer"
                aria-label="Visitar LinkedIn"
              >
                <FaLinkedinIn
                  size={18}
                  aria-hidden="true"
                />

                LinkedIn
              </a>
            )}

            {emailUrl && (
              <a
                href={emailUrl}
                aria-label="Enviar correo electrónico"
              >
                <Mail
                  size={18}
                  aria-hidden="true"
                />

                Email
              </a>
            )}
          </div>
        </motion.div>

        <motion.div
          className="portfolio-profile-visual"
          initial={{
            opacity: 0,
            x: 20,
          }}
          animate={{
            opacity: 1,
            x: 0,
          }}
          transition={{
            delay: 0.1,
            duration: 0.65,
            ease: [0.22, 1, 0.36, 1],
          }}
        >
          <div className="portfolio-profile-photo">
            {profile.profile_image_url ? (
              <img
                src={profile.profile_image_url}
                alt={`Fotografía profesional de ${profile.full_name}`}
              />
            ) : (
              <div
                className="portfolio-profile-fallback"
                aria-label={`Iniciales de ${profile.full_name}`}
              >
                <span>
                  {getInitials(profile.full_name)}
                </span>
              </div>
            )}

            <div className="portfolio-profile-badge">
              <span aria-hidden="true" />

              Disponible para oportunidades
            </div>
          </div>

          <div className="portfolio-hero__metrics">
            <article>
              <strong>{technologyCount}+</strong>
              <span>Tecnologías</span>
            </article>

            <article>
              <strong>{projectCount}</strong>
              <span>Proyectos</span>
            </article>

            <article>
              <strong>{experienceCount}</strong>
              <span>Experiencias</span>
            </article>
          </div>
        </motion.div>
      </div>
    </section>
  )
}