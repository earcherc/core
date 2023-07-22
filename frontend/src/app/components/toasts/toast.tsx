'use client';

import React, { useEffect, useRef, useState } from 'react';
import classNames from 'classnames';
import { CheckCircleIcon, XCircleIcon, ExclamationTriangleIcon, XMarkIcon } from '@heroicons/react/20/solid';
import useToast from './toast-context';

const Toast = ({ toast, index }: { toast: Toast; index: number }) => {
  const [isPaused, setIsPaused] = useState(false);
  const { removeToast } = useToast();
  const endTime = useRef<number>(0);
  const timerId = useRef<NodeJS.Timeout | null>(null);

  useEffect(() => {
    endTime.current = Date.now() + 5000;
    timerId.current = setTimeout(() => removeToast(index), 5000);

    return () => {
      if (timerId.current) {
        clearTimeout(timerId.current);
      }
    };
  }, [removeToast, index]);

  const pauseToast = () => {
    if (timerId.current) {
      clearTimeout(timerId.current);
      timerId.current = null;
    }

    // calculate the remaining time and store it
    const remainingTime = endTime.current - Date.now();
    endTime.current = Date.now() + remainingTime;
    setIsPaused(true);
  };

  const resumeToast = () => {
    if (!isPaused) return;

    const remainingTime = endTime.current - Date.now();
    timerId.current = setTimeout(() => removeToast(index), remainingTime);
    setIsPaused(false);
  };

  const toastTypeClasses: Record<string, ToastType> = {
    success: {
      bgColor: 'bg-green-50',
      textColor: 'text-green-800',
      progressColor: 'bg-green-500',
      icon: <CheckCircleIcon className="h-5 w-5 text-green-400" aria-hidden="true" />,
    },
    error: {
      bgColor: 'bg-red-50',
      textColor: 'text-red-800',
      progressColor: 'bg-red-500',
      icon: <XCircleIcon className="h-5 w-5 text-red-400" aria-hidden="true" />,
    },
    warning: {
      bgColor: 'bg-yellow-50',
      textColor: 'text-yellow-800',
      progressColor: 'bg-yellow-500',
      icon: <ExclamationTriangleIcon className="h-5 w-5 text-yellow-400" aria-hidden="true" />,
    },
    default: {
      bgColor: 'bg-gray-50',
      textColor: 'text-gray-800',
      progressColor: 'bg-gray-500',
      icon: null,
    },
  };

  const { bgColor, textColor, progressColor, icon } = toastTypeClasses[toast.type] || toastTypeClasses.default;

  return (
    <div
      onMouseEnter={pauseToast}
      onMouseLeave={resumeToast}
      className={classNames('relative w-1/2 rounded-md p-4', bgColor)}
    >
      <div className="flex">
        <div className="flex-shrink-0">{icon}</div>
        <div className="ml-3">
          <p className={classNames('text-sm font-medium', textColor)}>{toast.message}</p>
        </div>
        <div className="ml-auto pl-3">
          <div className="-mx-1.5 -my-1.5">
            <button
              onClick={() => removeToast(index)}
              type="button"
              className={classNames(
                'inline-flex rounded-md p-1.5',
                textColor,
                'hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-600 focus:ring-offset-2 focus:ring-offset-gray-50',
              )}
            >
              <span className="sr-only">Dismiss</span>
              <XMarkIcon className="h-5 w-5" aria-hidden="true" />
            </button>
          </div>
        </div>
      </div>
      <div
        className={classNames(progressColor, 'animate-countdown absolute bottom-0 left-0 h-1 w-full rounded-b-md ', {
          paused: isPaused,
        })}
      />
    </div>
  );
};

export default Toast;
