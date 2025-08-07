// export default function Home() {
//   return (
//     <div className="page-center">
//       <h2 className="page-title">Welcome to Movie Mood Matcher 🎥</h2>
//       <p className="subtitle">Discover movies that match your vibe, mood, and taste.</p>
//       <a href="/quiz" className="btn primary-btn">Take the Quiz</a>
//     </div>
//   );
// }

import './Home.css'; // We'll create this CSS file

export default function Home() {
  return (
    <div className="home-page">
      <div className="home-container">
        <h1 className="home-title">
          Movie Mood Matcher <span className="emoji">🎬</span>
        </h1>
        <p className="home-subtitle">
          Find your perfect movie match based on your current vibe, mood, and personal taste.
        </p>
        
        <div className="button-container">
          <a href="/quiz" className="primary-button">
            Start Quiz
          </a>
          <a href="/about" className="secondary-button">
            Learn More
          </a>
        </div>
        
        <div className="moods-container">
          {['😊', '😢', '🤩', '😨', '🤣', '💘'].map((emoji, i) => (
            <div key={i} className="mood-emoji">
              {emoji}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}