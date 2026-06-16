# 🎥 YouTube Video Summarizer

An AI-powered web app that summarizes any YouTube video instantly. Just paste a URL and get a clean summary in seconds.

## 🚀 Live Demo
[Click here to try it](https://youtube-summarizer-jvbgweepdxznwek32eahhx.streamlit.app/)

## ✨ Features
- Paste any YouTube URL and get an instant AI summary
- 3 summary formats: Concise, Detailed, and Bullet Points
- Download summary as a text file
- View full video transcript
- Clean dark themed UI
- Powered by LLaMA 3.3 70B via Groq (super fast)

## 🛠️ Tech Stack
| Tool | Purpose |
|---|---|
| Groq API | LLM inference (LLaMA 3.3 70B) |
| YouTube Transcript API | Fetching video transcripts |
| Streamlit | Web UI |
| Python | Core logic |

## ⚙️ Run Locally

1. Clone the repo
   git clone https://github.com/HiraArif666/youtube-summarizer.git
   cd youtube-summarizer

2. Create virtual environment
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Add your Groq API key in a .env file
   GROQ_API_KEY=your_key_here

5. Run the app
   streamlit run app.py

## 📸 How it Works
1. Paste a YouTube URL
2. Choose your preferred summary format
3. Click Summarize
4. Get your AI generated summary instantly
5. Download it or copy it

## 🔑 Get a Free Groq API Key
Visit https://console.groq.com to get your free API key.

## ⚠️ Note
Only works with YouTube videos that have captions/subtitles enabled.
Most educational, tech, and news videos have captions.
