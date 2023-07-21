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
      'x-api-key': process.env.API_KEY || '',
    },
    body: params,
  });

  const data = await res.json();

  return NextResponse.json(data);
}
