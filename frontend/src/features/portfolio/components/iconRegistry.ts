import type { ElementType } from 'react'
import {
  Blocks,
  BookOpen,
  Brain,
  BriefcaseBusiness,
  Code2,
  Database,
  Globe2,
  LayoutDashboard,
  Lightbulb,
  Mail,
  Music,
  RefreshCw,
  Server,
  Sparkles,
  Terminal,
  TestTube2,
  UserRound,
  Users,
  Workflow,
  Wrench,
} from 'lucide-react'
import {
  FaGithub,
  FaLinkedinIn,
} from 'react-icons/fa'

const icons: Record<string, ElementType> = {
  blocks: Blocks,
  'book-open': BookOpen,
  brain: Brain,
  briefcase: BriefcaseBusiness,
  code: Code2,
  code2: Code2,
  database: Database,

  github: FaGithub,
  linkedin: FaLinkedinIn,

  globe: Globe2,
  website: Globe2,
  'layout-dashboard': LayoutDashboard,
  layout: LayoutDashboard,
  lightbulb: Lightbulb,
  mail: Mail,
  email: Mail,
  music: Music,
  'refresh-cw': RefreshCw,
  server: Server,
  sparkles: Sparkles,
  terminal: Terminal,
  'test-tube': TestTube2,
  'user-round': UserRound,
  users: Users,
  workflow: Workflow,
  wrench: Wrench,
}

export function getPortfolioIcon(
  iconName: string,
): ElementType {
  const normalizedIconName = iconName
    .trim()
    .toLowerCase()

  return icons[normalizedIconName] ?? Code2
}