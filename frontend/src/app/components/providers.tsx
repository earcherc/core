'use client';

import ToastProvider from './toasts/toast-provider';

export function Providers({ children }: { children: React.ReactNode }) {
  return <ToastProvider>{children}</ToastProvider>;
}
