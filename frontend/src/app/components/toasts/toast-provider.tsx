'use client';

import { createContext, useCallback, useEffect, useState } from 'react';
import Toast from './toast';

export const ToastContext = createContext<IToastContext | undefined>(undefined);

export default function ToastProvider({ children }: { children: React.ReactNode }) {
  const [toasts, setToasts] = useState<Toast[]>([]);

  useEffect(() => {
    if (toasts.length > 0) {
      const timer = setTimeout(() => setToasts((toasts) => toasts.slice(1)), 5000);
      return () => clearTimeout(timer);
    }
  }, [toasts]);

  const addToast = useCallback(
    (toast: Toast) => {
      console.log(toast);
      setToasts((toasts) => [...toasts, toast]);
    },
    [setToasts],
  );

  return (
    <ToastContext.Provider value={{ addToast }}>
      {children}
      {toasts.map((toast: Toast, i: number) => (
        <Toast key={i} toast={toast} />
      ))}
    </ToastContext.Provider>
  );
}
