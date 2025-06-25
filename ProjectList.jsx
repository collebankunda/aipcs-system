
import React from 'react';

function ProjectList({ projects }) {
  return (
    <div className="space-y-4">
      {projects.map(project => (
        <div key={project.id} className="p-4 bg-gray-100 rounded shadow">
          <h3 className="text-lg font-bold">{project.name}</h3>
          <p>{project.location} — {project.client}</p>
          <p className="text-sm text-gray-600">Budget: UGX {project.budget}</p>
        </div>
      ))}
    </div>
  );
}

export default ProjectList;
