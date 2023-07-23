'use client';

import { useState, useEffect, createContext } from 'react';

export const AuthContext = createContext<IAuthContext | undefined>(undefined);

const AuthProvider = ({ children }: { children: React.ReactNode }) => {
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);
  const [username, setUsername] = useState<string | null>(null);
  const [userId, setUserId] = useState<number | null>(null);
  const [isDisabled, setIsDisabled] = useState<boolean | null>(null);

  useEffect(() => {
    const fetchAndSetUser = () => {
      const userCookie = document.cookie
        .split('; ')
        .find((row) => row.startsWith('user='))
        ?.split('=')[1];

      if (userCookie) {
        const { username, userId, isDisabled } = JSON.parse(decodeURIComponent(userCookie));
        setUsername(username);
        setUserId(userId);
        setIsDisabled(isDisabled);
        setIsAuthenticated(true);
      } else {
        setIsAuthenticated(false);
        setUsername(null);
        setUserId(null);
        setIsDisabled(null);
      }
    };

    fetchAndSetUser();
  }, []);

  return (
    <AuthContext.Provider value={{ isAuthenticated, username, userId, isDisabled }}>{children}</AuthContext.Provider>
  );
};

export default AuthProvider;
