import { NextRequest, NextResponse } from 'next/server';
import { verifyJwtToken } from '@libs/utils';

const PUBLIC_ROUTES = ['/login', '/register', '/'];
const isPublicPage = (url: string) => PUBLIC_ROUTES.some((page) => page.startsWith(url));

export async function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;
  const authCookie = request.cookies.get('jwt');

  const isPublicPageRequested = isPublicPage(pathname);
  const hasVerifiedToken = await verifyJwtToken(authCookie?.value);

  // If unprotected route just continue
  if (isPublicPageRequested) {
    return NextResponse.next();
  }

  // If the path is protected, we check the auth token
  if (!hasVerifiedToken) {
    return NextResponse.redirect('/login');
  }

  return NextResponse.next();
}
