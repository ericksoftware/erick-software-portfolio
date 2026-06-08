import {
  Route,
  Routes,
} from 'react-router'

import { HomePage } from '../features/portfolio/pages/HomePage'
import { ProjectDetailPage } from '../features/portfolio/pages/ProjectDetailPage'
import { NotFoundPage } from '../shared/components/NotFoundPage'

export function AppRouter() {
  return (
    <Routes>
      <Route
        path="/"
        element={<HomePage />}
      />

      <Route
        path="/projects/:slug"
        element={<ProjectDetailPage />}
      />

      <Route
        path="*"
        element={<NotFoundPage />}
      />
    </Routes>
  )
}