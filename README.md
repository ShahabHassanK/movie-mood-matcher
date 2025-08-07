# 🎬 Movie Mood Matcher

**Movie Mood Matcher** is a quiz-based movie recommendation web app that matches your **mood**, **preferences**, and **vibe** to a curated list of films using AI-powered embeddings.  
It’s fun, emoji-rich, and personalized — perfect for movie lovers looking for their next favorite film.

---

## 📽️ Live Demo

> ⚠️ Coming Soon  
> You can run it locally using the setup guide below.

---

## 🧠 How It Works

1. You take a 10-question quiz about your current mood, tastes, and preferences.
2. Your answers are mapped to a **63-dimensional trait vector**.
3. A trained **ML model** converts those traits into a **1512-dimensional movie embedding**.
4. The backend uses **cosine similarity** to find the closest movie vectors.
5. 🎉 You get the **top 5 movie recommendations**, including one **"best match"**.

---





## 🧪 Backend (FastAPI + ML)

### 🔧 Setup

```bash
cd backend
pip install -r requirements.txt
Make sure you have Python 3.8+ and uvicorn, fastapi, tensorflow, sentence-transformers, etc.

▶️ Run the Server
bash
Copy
Edit
uvicorn app.main:app --reload
Server runs at: http://localhost:8000

📬 API Endpoints
Endpoint	Method	Description
/api/questions	GET	Returns 15 random quiz questions
/api/recommend	POST	Takes 15 answers and returns 5 recommendations



🎨 Frontend (React)

cd frontend
npm install
▶️ Run the App

npm run dev
Frontend runs at: http://localhost:5173

📌 Pages
Route	Description
/	Home page with intro CTA
/quiz	Quiz page with 10=5 emoji questions
/recommendations	Results page with top 5 movies
/about	Info page about the app



🛠️ Environment Variables
Create a .env file in backend/ with:


TMDB_API_KEY=<your_tmdb_api_key>      # optional if fetching posters, etc.
📦 Requirements
Backend:
fastapi

uvicorn

tensorflow

sentence-transformers

scikit-learn

pandas, numpy, etc.

Frontend:
react

vite

react-router-dom

axios



✨ Features Summary
✅ 15-question quiz with emojis
✅ FastAPI ML backend
✅ Cosine Similarity Recommendation engine
✅ Sentence Transformers and Prompt Generation
✅ Clean, responsive frontend UI
✅ Top 5 personalized movie matches



🙌 Acknowledgments
MovieLens + TMDb for the movie data

HuggingFace for sentence-transformers

FastAPI & React communities for awesome tools
