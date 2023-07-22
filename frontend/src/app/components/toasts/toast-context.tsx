import { useContext } from 'react';
import { ToastContext } from './toast-provider';

export default function useToast(): IToastContext {
  const context = useContext(ToastContext);

  if (!context) {
    throw new Error('useToast must be used within a ToastProvider');
  }

  return context;
}
