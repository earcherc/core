'use client';

import { useState, createContext, useEffect } from 'react';

export const AuthContext = createContext<IAuthContext | undefined>(undefined);

const AuthProvider = ({ children }: { children: React.ReactNode }) => {
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);
  const [username, setUsername] = useState<string | null>(null);
  const [userId, setUserId] = useState<number | null>(null);
  const [isDisabled, setIsDisabled] = useState<boolean | null>(null);

  const setUser = ({ username, userId, isDisabled }: UserData) => {
    setUsername(username);
    setUserId(userId);
    setIsDisabled(isDisabled);
    setIsAuthenticated(true);
  };

  const clearUser = () => {
    setIsAuthenticated(false);
    setUsername(null);
    setUserId(null);
    setIsDisabled(null);
  };

  const isValidUser = (user: UserData): user is UserData => {
    return (
      user &&
      typeof user.username === 'string' &&
      typeof user.userId === 'number' &&
      typeof user.isDisabled === 'boolean'
    );
  };

  useEffect(() => {
    const userCookie = document.cookie
      .split('; ')
      .find((row) => row.startsWith('user='))
      ?.split('=')[1];

    if (userCookie) {
      const user = JSON.parse(decodeURIComponent(userCookie));
      if (isValidUser(user)) {
        setUser(user);
      } else {
        console.error('Invalid user data in cookie:', user);
        clearUser();
      }
    } else {
      clearUser();
    }
  }, []);

  return (
    <AuthContext.Provider value={{ isAuthenticated, username, userId, isDisabled, setUser, clearUser }}>
      {children}
    </AuthContext.Provider>
  );
};

export default AuthProvider;
