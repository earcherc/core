'use client';

import { createContext, useCallback, useState } from 'react';
import Toast from './toast';

export const ToastContext = createContext<IToastContext | undefined>(undefined);

export default function ToastProvider({ children }: { children: React.ReactNode }) {
  const [toasts, setToasts] = useState<Toast[]>([]);

  const addToast = useCallback(
    (toast: Toast) => {
      setToasts((toasts) => [...toasts, toast]);
    },
    [setToasts],
  );

  const removeToast = useCallback(
    (index: number) => {
      setToasts((toasts) => toasts.filter((_, i) => i !== index));
    },
    [setToasts],
  );

  return (
    <ToastContext.Provider value={{ addToast, removeToast }}>
      {children}
      <div className="fixed left-0 right-0 top-0 z-50 flex flex-col items-center space-y-1">
        {toasts.map((toast: Toast, i: number) => (
          <Toast key={i} toast={toast} index={i} />
        ))}
      </div>
    </ToastContext.Provider>
  );
}
