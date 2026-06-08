export interface SiteProfile {
  full_name: string
  professional_title: string
  hero_eyebrow: string
  hero_summary: string
  about_text: string
  work_philosophy: string
  technology_interests: string
  profile_image_url: string | null
  resume_url: string | null
  contact_email: string
  location: string
  availability_text: string
  contact_cta_title: string
  contact_cta_text: string
}

export interface SectionSettings {
  key:
    | 'hero'
    | 'about'
    | 'stack'
    | 'experience'
    | 'projects'
    | 'education'
    | 'contact'
  label: string
  navigation_label: string
  eyebrow: string
  title: string
  description: string
  order: number
}

export interface SocialLink {
  id: number
  platform: string
  platform_label: string
  label: string
  url: string
  icon_name: string
  open_in_new_tab: boolean
  order: number
}

export interface Technology {
  id: number
  name: string
  slug: string
  icon_name: string
  official_url: string
  is_featured: boolean
  order: number
}

export interface TechnologyCategory {
  id: number
  name: string
  slug: string
  description: string
  icon_name: string
  order: number
  technologies: Technology[]
}

export interface ProfessionalStrength {
  id: number
  title: string
  description: string
  icon_name: string
  order: number
}

export interface Experience {
  id: number
  role: string
  company: string
  company_url: string
  location: string
  start_date: string | null
  end_date: string | null
  is_current: boolean
  period_label: string
  summary: string
  impact: string
  technologies: Technology[]
  order: number
}

export type ProjectStatus =
  | 'development'
  | 'active'
  | 'completed'
  | 'maintenance'
  | 'archived'

export interface Project {
  id: number
  title: string
  slug: string
  short_description: string
  role: string
  impact: string
  status: ProjectStatus
  status_label: string
  cover_image_url: string | null
  demo_url: string
  repository_url: string
  project_url: string
  is_repository_private: boolean
  is_featured: boolean
  started_at: string | null
  completed_at: string | null
  technologies: Technology[]
  order: number
}

export interface ProjectImage {
  id: number
  image_url: string | null
  alt_text: string
  caption: string
  order: number
}

export interface ProjectDetail extends Project {
  description: string
  gallery: ProjectImage[]
}

export interface Education {
  id: number
  institution: string
  program: string
  location: string
  start_date: string | null
  end_date: string | null
  is_current: boolean
  period_label: string | null
  description: string
  institution_url: string
  logo_url: string | null
  order: number
}

export interface Certification {
  id: number
  name: string
  issuer: string
  issue_date: string | null
  expiration_date: string | null
  credential_id: string
  credential_url: string
  image_url: string | null
  order: number
}

export interface SidebarLink {
  id: number
  title: string
  description: string
  url: string
  icon_name: string
  badge_text: string
  open_in_new_tab: boolean
  order: number
}

export interface SeoSettings {
  site_title: string
  meta_description: string
  keywords: string
  canonical_url: string
  og_image_url: string | null
  robots_index: boolean
}

export interface PortfolioData {
  profile: SiteProfile | null
  sections: SectionSettings[]
  social_links: SocialLink[]
  technology_categories: TechnologyCategory[]
  strengths: ProfessionalStrength[]
  experiences: Experience[]
  featured_projects: Project[]
  education: Education[]
  certifications: Certification[]
  sidebar_links: SidebarLink[]
  seo: SeoSettings | null
}