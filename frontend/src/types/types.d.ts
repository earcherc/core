declare type Toast = {
  type: string;
  message: string;
};

declare interface ToastType {
  bgColor: string;
  textColor: string;
  progressColor: string;
  icon: ReactElement | null;
}

declare interface IToastContext {
  addToast: (toast: Toast) => void;
  removeToast: (id: number) => void;
}
