// import React, { useEffect, useState } from 'react';
// import { useNavigate } from 'react-router-dom';

// export default function Quiz() {
//   const [questions, setQuestions] = useState([]);
//   const [answers, setAnswers] = useState({});
//   const [loading, setLoading] = useState(true);
//   const [error, setError] = useState(null);
//   const navigate = useNavigate();

//   useEffect(() => {
//     const fetchQuestions = async () => {
//       try {
//         const response = await fetch('http://localhost:8000/api/api/questions');
//         if (!response.ok) throw new Error('Network response was not ok');
        
//         const data = await response.json();
        
//         // Verify the data structure contains traits
//         const verifiedQuestions = data.map((q, index) => {
//           // Ensure options have both text and traits
//           const options = q.options.map(opt => {
//             if (typeof opt === 'string') {
//               console.warn(`Option is string instead of object: ${opt}`);
//               return { text: opt, traits: [] };
//             }
//             return {
//               text: opt.text,
//               traits: opt.traits || [] // Fallback to empty array
//             };
//           });
          
//           return {
//             id: index,
//             question: q.question,
//             options: options
//           };
//         });

//         setQuestions(verifiedQuestions);
//       } catch (err) {
//         console.error('Failed to load questions:', err);
//         setError('Failed to load questions. Please try again later.');
//       } finally {
//         setLoading(false);
//       }
//     };

//     fetchQuestions();
//   }, []);

//   const handleAnswer = (questionId, optionIndex) => {
//     setAnswers(prev => ({ ...prev, [questionId]: optionIndex }));
//   };

//   const handleSubmit = () => {
//     // Extract all selected traits
//     const allTraits = questions.flatMap(q => {
//       const selectedOptionIndex = answers[q.id];
//       if (selectedOptionIndex === undefined) return [];
//       return q.options[selectedOptionIndex].traits;
//     });

//     if (allTraits.length === 0) {
//       alert('No traits were selected. This suggests a problem with the questions data.');
//       return;
//     }

//     fetch('http://localhost:8000/api/api/recommend', {
//       method: 'POST',
//       headers: { 'Content-Type': 'application/json' },
//       body: JSON.stringify({
//         traits: allTraits,
//         top_n: 5
//       })
//     })
//     .then(async res => {
//       if (!res.ok) {
//         const errorData = await res.json().catch(() => ({}));
//         throw new Error(errorData.detail || 'Failed to get recommendations');
//       }
//       return res.json();
//     })
//     .then(data => {
//       navigate('/recommendations', { state: { results: data.recommendations } });
//     })
//     .catch(err => {
//       console.error('Recommendation error:', err);
//       alert(err.message || 'Failed to get recommendations');
//     });
//   };

//   if (loading) return <div>Loading questions...</div>;
//   if (error) return <div className="error">{error}</div>;

//   return (
//     <div className="quiz">
//       <h1>Movie Mood Quiz</h1>
      
//       {questions.map((q, qIndex) => (
//         <div key={q.id} className="question">
//           <h3>{qIndex + 1}. {q.question}</h3>
          
//           <div className="options">
//             {q.options.map((opt, optIndex) => (
//               <div 
//                 key={optIndex}
//                 className={`option ${answers[q.id] === optIndex ? 'selected' : ''}`}
//                 onClick={() => handleAnswer(q.id, optIndex)}
//               >
//                 <input
//                   type="radio"
//                   name={`question-${q.id}`}
//                   checked={answers[q.id] === optIndex}
//                   readOnly
//                 />
//                 <span>{opt.text}</span>
//               </div>
//             ))}
//           </div>
//         </div>
//       ))}

//       <button 
//         onClick={handleSubmit}
//         disabled={Object.keys(answers).length !== questions.length}
//       >
//         Get Recommendations
//       </button>
//     </div>
//   );
// }

import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

export default function Quiz() {
  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState({});
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [progress, setProgress] = useState(0);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchQuestions = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/api/questions');
        if (!response.ok) throw new Error('Network response was not ok');
        
        const data = await response.json();
        
        const verifiedQuestions = data.map((q, index) => {
          const options = q.options.map(opt => {
            if (typeof opt === 'string') {
              console.warn(`Option is string instead of object: ${opt}`);
              return { text: opt, traits: [] };
            }
            return {
              text: opt.text,
              traits: opt.traits || []
            };
          });
          
          return {
            id: index,
            question: q.question,
            options: options
          };
        });

        setQuestions(verifiedQuestions);
        setProgress(100 / verifiedQuestions.length);
      } catch (err) {
        console.error('Failed to load questions:', err);
        setError('Failed to load questions. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    fetchQuestions();
  }, []);

  const handleAnswer = (optionIndex) => {
    setAnswers(prev => ({
      ...prev,
      [questions[currentQuestionIndex].id]: optionIndex
    }));
    
    // Auto-advance to next question after selection
    setTimeout(() => {
      if (currentQuestionIndex < questions.length - 1) {
        goToNextQuestion();
      }
    }, 300);
  };

  const goToNextQuestion = () => {
    if (currentQuestionIndex < questions.length - 1) {
      setCurrentQuestionIndex(prev => prev + 1);
      setProgress(((currentQuestionIndex + 1) / questions.length) * 100);
    }
  };

  const goToPrevQuestion = () => {
    if (currentQuestionIndex > 0) {
      setCurrentQuestionIndex(prev => prev - 1);
      setProgress(((currentQuestionIndex - 1) / questions.length) * 100);
    }
  };

  const handleSubmit = () => {
    const allTraits = questions.flatMap(q => {
      const selectedOptionIndex = answers[q.id];
      if (selectedOptionIndex === undefined) return [];
      return q.options[selectedOptionIndex].traits;
    });

    if (allTraits.length === 0) {
      alert('No traits were selected. Please answer at least one question.');
      return;
    }

    fetch('http://localhost:8000/api/api/recommend', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        traits: allTraits,
        top_n: 5
      })
    })
    .then(async res => {
      if (!res.ok) {
        const errorData = await res.json().catch(() => ({}));
        throw new Error(errorData.detail || 'Failed to get recommendations');
      }
      return res.json();
    })
    .then(data => {
      navigate('/recommendations', { state: { results: data.recommendations } });
    })
    .catch(err => {
      console.error('Recommendation error:', err);
      alert(err.message || 'Failed to get recommendations');
    });
  };

  if (loading) {
    return (
      <div className="loading-screen">
        <div className="spinner"></div>
        <p>Loading your movie quiz...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="error-screen">
        <div className="error-icon">⚠️</div>
        <p>{error}</p>
        <button onClick={() => window.location.reload()} className="retry-btn">
          Try Again
        </button>
      </div>
    );
  }

  if (questions.length === 0) {
    return (
      <div className="no-questions">
        <p>No questions available at the moment.</p>
      </div>
    );
  }

  const currentQuestion = questions[currentQuestionIndex];
  const selectedOption = answers[currentQuestion.id];

  return (
    <div className="quiz-container">
      <div className="progress-bar">
        <div 
          className="progress-fill" 
          style={{ width: `${progress}%` }}
        ></div>
        <span className="progress-text">
          Question {currentQuestionIndex + 1} of {questions.length}
        </span>
      </div>

      <div className="question-card">
        <h2 className="question-text">{currentQuestion.question}</h2>
        
        <div className="options-grid">
          {currentQuestion.options.map((opt, optIndex) => (
            <button
              key={optIndex}
              className={`option-btn ${selectedOption === optIndex ? 'selected' : ''}`}
              onClick={() => handleAnswer(optIndex)}
            >
              <span className="option-emoji">
                {opt.text.match(/[\p{Emoji}]/gu)?.[0] || '🎬'}
              </span>
              <span className="option-text">
                {opt.text.replace(/[\p{Emoji}]/gu, '').trim()}
              </span>
            </button>
          ))}
        </div>
      </div>

      <div className="navigation-btns">
        <button
          onClick={goToPrevQuestion}
          disabled={currentQuestionIndex === 0}
          className="nav-btn prev-btn"
        >
          ← Previous
        </button>
        
        {currentQuestionIndex < questions.length - 1 ? (
          <button
            onClick={goToNextQuestion}
            disabled={selectedOption === undefined}
            className="nav-btn next-btn"
          >
            Next →
          </button>
        ) : (
          <button
            onClick={handleSubmit}
            disabled={selectedOption === undefined}
            className="submit-btn"
          >
            🎉 Get My Recommendations
          </button>
        )}
      </div>
    </div>
  );
}