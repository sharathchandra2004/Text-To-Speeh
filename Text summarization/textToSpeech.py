import streamlit as st
import pyttsx3

# Function to convert text to speech
def text_to_speech(text, rate, volume, voice_id):
    # Create a new instance of the TTS engine each time
    engine = pyttsx3.init()
    
    # Set properties
    engine.setProperty('rate', rate)   # Speed of speech
    engine.setProperty('volume', volume)  # Volume (0.0 to 1.0)
    engine.setProperty('voice', voice_id)  # Voice (male/female)
    
    # Speak the text
    engine.say(text)
    engine.runAndWait()
    engine.stop()  # Safely stop the engine to prevent conflicts

# Streamlit App
st.set_page_config(page_title="Text-to-Speech", page_icon="🔊", layout="centered")
st.title("🔊 Text-to-Speech Converter")

# User input for text
text = st.text_area("Enter the text to convert to speech", height=200)

# TTS Settings
st.sidebar.header("TTS Settings")
rate = st.sidebar.slider("Speech Rate (words per minute)", min_value=50, max_value=300, value=150)
volume = st.sidebar.slider("Volume", min_value=0.0, max_value=1.0, value=1.0)

# Voice Selection
engine = pyttsx3.init()  # Temporary instance to fetch voice options
voices = engine.getProperty("voices")
voice_options = [f"{voice.id} ({voice.name})" for voice in voices]
selected_voice = st.sidebar.selectbox("Select Voice", voice_options)
voice_id = voices[voice_options.index(selected_voice)].id

# Button to trigger TTS
if st.button("Convert to Speech"):
    if text.strip():
        st.success("Speaking the text...")
        text_to_speech(text, rate, volume, voice_id)
    else:
        st.error("Please enter some text to convert.")

st.info("Adjust settings in the sidebar and click 'Convert to Speech'.")
