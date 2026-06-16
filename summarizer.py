import os
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import WebshareProxyConfig
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def extract_video_id(url):
    """Extract video ID from various YouTube URL formats"""
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    else:
        return None


def get_transcript(video_id):
    """Fetch transcript from YouTube"""
    try:
        ytt_api = YouTubeTranscriptApi()
        fetched = ytt_api.fetch(video_id)
        transcript = " ".join([t.text for t in fetched])
        return transcript
    except Exception as e:
        print(f"Transcript error: {e}")
        return None


def summarize_transcript(transcript, summary_type="concise"):
    """Summarize the transcript using Groq"""

    if summary_type == "concise":
        prompt = f"""Summarize the following YouTube video transcript in a concise paragraph of 5-7 sentences.
Focus on the main points and key takeaways.

Transcript:
{transcript[:8000]}

Summary:"""

    elif summary_type == "detailed":
        prompt = f"""Summarize the following YouTube video transcript in detail.
Structure your summary with:
- **Main Topic**
- **Key Points** (bullet points)
- **Important Details**
- **Conclusion**

Transcript:
{transcript[:8000]}

Summary:"""

    elif summary_type == "bullets":
        prompt = f"""Extract the key points from the following YouTube video transcript.
Return exactly 5-8 bullet points covering the most important information.

Transcript:
{transcript[:8000]}

Key Points:"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000
    )

    return response.choices[0].message.content