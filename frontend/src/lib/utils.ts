import { NextResponse } from 'next/server';

/**
 * Returns a Response object with a JSON body
 */
// eslint-disable-next-line @typescript-eslint/no-explicit-any
export function jsonResponse(status: number, data: any, init?: ResponseInit) {
  return new NextResponse(JSON.stringify(data), {
    ...init,
    status,
    headers: {
      ...init?.headers,
      'Content-Type': 'application/json',
    },
  });
}
