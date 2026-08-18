import { createContext, useState } from 'react';
import api from '../api';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const login = async (username, password) => {
    const res = await api.post('token/', { username, password });
    localStorage.setItem('access_token', res.data.access);
    localStorage.setItem('refresh_token', res.data.refresh);
    // fetch user
  };
  const logout = () => { localStorage.clear(); setUser(null); };
  // ...
};