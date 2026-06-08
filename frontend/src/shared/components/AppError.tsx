import { AlertTriangle, RefreshCw } from 'lucide-react'

interface AppErrorProps {
  title?: string
  message?: string
}

export function AppError({
  title = 'No pudimos cargar el contenido',
  message = (
    'Verifica que el servidor de Django esté ejecutándose '
    + 'e inténtalo nuevamente.'
  ),
}: AppErrorProps) {
  function reloadPage(): void {
    window.location.reload()
  }

  return (
    <main className="app-state">
      <section
        className="error-card"
        role="alert"
      >
        <span className="error-card__icon">
          <AlertTriangle aria-hidden="true" />
        </span>

        <p className="eyebrow">
          Error de conexión
        </p>

        <h1>{title}</h1>

        <p>{message}</p>

        <button
          type="button"
          className="button button--primary"
          onClick={reloadPage}
        >
          <RefreshCw
            size={18}
            aria-hidden="true"
          />

          Reintentar
        </button>
      </section>
    </main>
  )
}