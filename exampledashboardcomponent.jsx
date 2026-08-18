import { AuthContext } from '../context/AuthContext';
import { useContext } from 'react';
import { DashboardLayout } from '../components/DashboardLayout';

export default function AdminOverview() {
  const { user } = useContext(AuthContext);
  // fetch stats from API
  return (
    <DashboardLayout>
      <h1>Welcome, {user?.full_name}</h1>
      {/* stats cards, tables, etc. */}
    </DashboardLayout>
  );
}