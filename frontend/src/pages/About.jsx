export default function About() {
  return (
    <div className="about-page">
      <div className="about-container">
        <h1 className="about-title">
          <span>About Movie Mood Matcher</span>
          <span className="title-emoji">🎭</span>
        </h1>
        
        <div className="about-content">
          <div className="about-section">
            <p>
              Movie Mood Matcher is an innovative platform that combines psychology with entertainment to help you discover films that perfectly match your current emotional state and preferences.
            </p>
          </div>
          
          <div className="about-section">
            <h2 className="section-title">How It Works</h2>
            <ul className="about-list">
              <li>Take our quick mood assessment quiz</li>
              <li>Our AI analyzes your responses and current trends</li>
              <li>Get personalized movie recommendations</li>
              <li>Save your favorites and discover new gems</li>
            </ul>
          </div>
          
          <div className="about-section">
            <h2 className="section-title">Our Mission</h2>
            <p>
              We believe there's a perfect movie for every mood. Whether you're feeling nostalgic, adventurous, or just need a good cry, we'll help you find exactly what you're looking for.
            </p>
          </div>
          
          <a href="/" className="back-button">
            ← Back to Home
          </a>
        </div>
      </div>
    </div>
  );
}