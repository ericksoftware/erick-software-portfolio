function getRequiredEnvironmentVariable(
  name: keyof ImportMetaEnv,
): string {
  const value = import.meta.env[name]

  if (!value || !value.trim()) {
    throw new Error(
      `La variable de entorno ${name} no está configurada.`,
    )
  }

  return value.replace(/\/+$/, '')
}

export const env = {
  apiBaseUrl: getRequiredEnvironmentVariable(
    'VITE_API_BASE_URL',
  ),
} as const