import { env } from '../config/env'

export class ApiError extends Error {
  readonly status: number
  readonly details: unknown

  constructor(
    message: string,
    status: number,
    details: unknown = null,
  ) {
    super(message)

    this.name = 'ApiError'
    this.status = status
    this.details = details
  }
}

type ApiRequestOptions = RequestInit & {
  signal?: AbortSignal
}

async function parseResponseBody(
  response: Response,
): Promise<unknown> {
  const contentType = response.headers.get('content-type')

  if (contentType?.includes('application/json')) {
    return response.json()
  }

  const text = await response.text()

  return text || null
}

export async function apiRequest<T>(
  endpoint: string,
  options: ApiRequestOptions = {},
): Promise<T> {
  const normalizedEndpoint = endpoint.startsWith('/')
    ? endpoint
    : `/${endpoint}`

  const response = await fetch(
    `${env.apiBaseUrl}${normalizedEndpoint}`,
    {
      ...options,
      headers: {
        Accept: 'application/json',
        ...options.headers,
      },
    },
  )

  const responseBody = await parseResponseBody(response)

  if (!response.ok) {
    throw new ApiError(
      `La solicitud falló con estado ${response.status}.`,
      response.status,
      responseBody,
    )
  }

  return responseBody as T
}