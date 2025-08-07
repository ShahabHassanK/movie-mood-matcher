// // movie-mood-matcher/frontend/src/pages/Recommendations.jsx

// import { useLocation } from 'react-router-dom';

// export default function Recommendations() {
//   const location = useLocation();
//   const results = location.state?.results;

//   if (!Array.isArray(results) || results.length === 0) {
//     return <p>No recommendations available. Please take the quiz first.</p>;
//   }

//   return (
//     <div>
//       <h2 className="page-title">🎬 Your Movie Recommendations</h2>
//       <div className="recommendation-grid">
//         {results.map((movie, index) => (
//           <div key={`${movie.title}-${movie.year}`} className="movie-card">
//             <h3 className="movie-title">
//               {index === 0 ? '⭐ Best Match: ' : ''}
//               {movie.title} ({movie.year})
//             </h3>
//             <p className="movie-overview">{movie.overview}</p>
//           </div>
//         ))}
//       </div>
//     </div>
//   );
// }

import { useLocation } from 'react-router-dom';
import './Recommendations.css'; // Create this CSS file

export default function Recommendations() {
  const location = useLocation();
  const results = location.state?.results;

  if (!Array.isArray(results) || results.length === 0) {
    return (
      <div className="no-results">
        <p>No recommendations available. Please take the quiz first.</p>
      </div>
    );
  }

  return (
    <div className="recommendations-page">
      <div className="recommendations-container">
        <div className="recommendations-header">
          <h1>🎬 Your Movie Recommendations</h1>
          <p className="subtitle">Based on your mood and preferences</p>
        </div>

        <div className="movies-list">
          {results.map((movie, index) => (
            <div 
              key={`${movie.title}-${movie.year}`} 
              className={`movie-card ${index === 0 ? 'best-match' : ''}`}
            >
              <h2 className={index === 0 ? 'best-match-title' : 'movie-title'}>
                {index === 0 ? (
                  <span className="best-match-header">
                    <span className="star-icon">⭐</span> Best Match: {movie.title} ({movie.year})
                  </span>
                ) : (
                  `${movie.title} (${movie.year})`
                )}
              </h2>
              <p className="movie-overview">{movie.overview}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}