import { ArrowLeft } from 'lucide-react'
import { Link } from 'react-router'

export function NotFoundPage() {
  return (
    <main className="app-state">
      <section className="error-card">
        <p className="eyebrow">
          Error 404
        </p>

        <h1>Página no encontrada</h1>

        <p>
          La dirección solicitada no existe o fue movida.
        </p>

        <Link
          to="/"
          className="button button--primary"
        >
          <ArrowLeft
            size={18}
            aria-hidden="true"
          />

          Volver al portfolio
        </Link>
      </section>
    </main>
  )
}