import streamlit as st
from utils.video_utils import extract_audio_from_url
from utils.audio_utils import transcribe_audio
from utils.accent_model import classify_accent

st.title("English Accent Classification Tool BY Issa Sukatu Abdullahi(sukaissa@gmail.com)")

video_url = st.text_input("Enter Video URL")
uploaded_file = st.file_uploader("Or browse for a video/audio file", type=["mp4", "mp3", "wav", "m4a"])

audio_path = None

if video_url:
    with st.spinner("Processing video from URL..."):
        audio_path = extract_audio_from_url(video_url)
elif uploaded_file is not None:
    with st.spinner("Processing uploaded file..."):
        # Save uploaded file to a temp location
        import tempfile, os
        suffix = "." + uploaded_file.name.split(".")[-1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(uploaded_file.read())
            audio_path = tmp.name

if audio_path:
    transcript = transcribe_audio(audio_path)
    accent, confidence, summary = classify_accent(transcript)
    st.success("Analysis Complete")
    st.markdown(f"**Transcript:** {transcript}")
    st.markdown(f"**Predicted Accent:** {accent}")
    st.markdown(f"**Confidence:** {confidence}%")
    if summary:
        st.markdown(f"**Explanation:** {summary}")
