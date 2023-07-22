import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  const { username, password } = await request.json();

  const params = new URLSearchParams();
  params.append('username', username);
  params.append('password', password);

  const res = await fetch('http://localhost:8002/auth/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
      'x-api-key': process.env.API_KEY ?? '',
    },
    body: params,
  });

  if (!res.ok) {
    const body = await res.json();
    return NextResponse.json({ body, status: 500 });
  }

  const body = await res.json();

  const cookie = {
    name: 'jwt',
    value: body.access_token,
    maxAge: 60 * 60,
    httpOnly: true,
  };

  const response = NextResponse.json({ body, status: 200 });
  response.cookies.set(cookie);

  return response;
}
