
import React from 'react';

function DashboardCard({ label, value, color }) {
  return (
    <div className={`p-4 rounded shadow text-white ${color}`}>
      <h4 className="text-sm">{label}</h4>
      <p className="text-xl font-bold">{value}</p>
    </div>
  );
}

export default DashboardCard;
