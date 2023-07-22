declare type Toast = {
  type: string;
  message: string;
};

declare interface ToastType {
  bgColor: string;
  textColor: string;
  icon: ReactElement | null;
}

declare interface IToastContext {
  addToast: (toast: Toast) => void;
}
