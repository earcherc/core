declare type Toast = {
  id: string;
  type: string;
  content: string; // Or JSX.Element
  autoCloseDelay: number;
  remainingTime: number;
  isPaused: boolean;
};

declare interface ToastType {
  bgColor: string;
  textColor: string;
  progressColor: string;
  icon: ReactElement | null;
}

declare interface IToastContext {
  toasts: Toast[];
  addToast: (toast: Pick<Toast, 'type' | 'content'>) => void;
  removeToast: (id: string) => void;
  pauseToast: (id: string) => void;
  resumeToast: (id: string) => void;
}
