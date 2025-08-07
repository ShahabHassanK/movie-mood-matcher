import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Home from './pages/Home';
import Quiz from './pages/Quiz';
import Recommendations from './pages/Recommendations';
import About from './pages/About';
import './App.css';

function App() {
  return (
    <Router>
      <div className="app-container">
        <header className="app-header">
          <h1 className="logo">🎬 Movie Mood Matcher</h1>
          <nav className="nav-links">
            <Link to="/">Home</Link>
            <Link to="/quiz">Quiz</Link>
            <Link to="/recommendations">Recommendations</Link>
            <Link to="/about">About</Link>
          </nav>
        </header>

        <main className="app-main">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/quiz" element={<Quiz />} />
            <Route path="/recommendations" element={<Recommendations />} />
            <Route path="/about" element={<About />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
