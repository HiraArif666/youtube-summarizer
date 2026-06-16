import streamlit as st
from summarizer import extract_video_id, get_transcript, summarize_transcript

st.set_page_config(
    page_title="YouTube Summarizer",
    page_icon="🎥",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
        .stApp {
            background-color: #0f1117;
            color: #ffffff;
        }
        [data-testid="stSidebar"] {
            background-color: #1a1d27;
            border-right: 1px solid #2e3250;
        }
        [data-testid="stAlert"] {
            border-radius: 10px;
        }
        .summary-box {
            background-color: #1e2130;
            border-radius: 12px;
            padding: 20px;
            border: 1px solid #2e3250;
            margin-top: 20px;
        }
        h1 {
            color: #ff4757;
            font-size: 2rem;
            font-weight: 700;
        }
        hr {
            border-color: #2e3250;
        }
        [data-testid="stTextInput"] input {
            background-color: #1e2130;
            border-radius: 10px;
            border: 1px solid #2e3250;
            color: #ffffff;
        }
    </style>
""", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🎥 YouTube Summarizer")
    st.markdown("---")
    st.markdown("### ⚙️ Summary Type")

    summary_type = st.radio(
        "Choose format:",
        options=["concise", "detailed", "bullets"],
        format_func=lambda x: {
            "concise": "📝 Concise Paragraph",
            "detailed": "📋 Detailed Breakdown",
            "bullets": "🔹 Bullet Points"
        }[x]
    )

    st.markdown("---")
    st.markdown("### ℹ️ How to use")
    st.markdown("""
    1. Paste a YouTube URL
    2. Choose summary type
    3. Click Summarize
    4. Read your summary!
    """)
    st.markdown("---")
    st.markdown("Built with Groq + LLaMA 3.3 70B")

# ── Main Area ─────────────────────────────────────────────
st.markdown("# 🎥 YouTube Video Summarizer")
st.markdown("Paste any YouTube URL and get an instant AI summary.")
st.markdown("---")

url = st.text_input(
    "YouTube URL",
    placeholder="https://www.youtube.com/watch?v=..."
)

col1, col2, col3 = st.columns([1, 1, 3])
with col1:
    summarize_btn = st.button("⚡ Summarize", use_container_width=True)
with col2:
    if st.button("🗑️ Clear", use_container_width=True):
        st.session_state.summary = None
        st.session_state.transcript = None
        st.rerun()

# ── Summarize Logic ───────────────────────────────────────
if summarize_btn:
    if not url:
        st.warning("⚠️ Please paste a YouTube URL first!")
    else:
        video_id = extract_video_id(url)

        if not video_id:
            st.error("❌ Invalid YouTube URL. Please check and try again.")
        else:
            with st.spinner("📥 Fetching transcript..."):
                transcript = get_transcript(video_id)

            if transcript is None:
                st.error("❌ Could not fetch transcript. The video may not have captions enabled.")
            else:
                with st.spinner("🤖 Summarizing..."):
                    summary = summarize_transcript(transcript, summary_type)
                    st.session_state.summary = summary
                    st.session_state.transcript = transcript

# ── Display Summary ───────────────────────────────────────
if "summary" in st.session_state and st.session_state.summary:
    st.markdown("### 📄 Summary")
    st.markdown(
        f"<div class='summary-box'>{st.session_state.summary}</div>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.download_button(
            label="📥 Download Summary",
            data=st.session_state.summary,
            file_name="summary.txt",
            mime="text/plain",
            use_container_width=True
        )
    with col2:
        with st.expander("📜 View Full Transcript"):
            st.text(st.session_state.transcript[:3000] + "...")