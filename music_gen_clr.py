import streamlit as st
import torchaudio
from audiocraft.models import MusicGen
import tempfile

# Load model
model = MusicGen.get_pretrained('melody')

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #fffbe6;
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }
        .stApp {
            background-image: linear-gradient(to right, #ffecd2 0%, #fcb69f 100%);
            padding: 20px;
        }
        .title {
            color: #6a0dad;
            font-size: 42px;
            text-align: center;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #444;
            margin-bottom: 30px;
        }
        .radio, .selectbox, .text-area, .button {
            background-color: #ffffffdd;
            border-radius: 10px;
            padding: 10px;
        }
        .footer {
            font-size: 12px;
            text-align: center;
            color: gray;
            margin-top: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.markdown('<div class="title">🎼 AI Music Time Machine</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Convert lyrics or a melody into music from another decade! 🎶✨</div>', unsafe_allow_html=True)

# Widgets with emoji enhancements
input_type = st.radio("🎤 Choose Input Type", ["Lyrics", "Melody (Upload WAV)"])
decade = st.selectbox("🕰️ Choose a Decade Style", ["1920s Jazz", "1980s Synthwave", "2000s Hip-Hop", "2010s EDM"])

if input_type == "Lyrics":
    lyrics = st.text_area("📝 Enter Lyrics or Prompt", placeholder="Type your magical lyrics here...")

if input_type == "Melody (Upload WAV)":
    uploaded_file = st.file_uploader("🎵 Upload melody file (WAV format)", type=["wav"])

# Generate Button
if st.button("🚀 Time Travel! Generate Music"):
    with st.spinner("🎶 Generating music... Hold on to your headphones!"):

        # Style prompt
        style_map = {
            "1920s Jazz": "jazz band in 1920s style with trumpets, clarinet, swing rhythm",
            "1980s Synthwave": "1980s synthwave track with retro electronic beats",
            "2000s Hip-Hop": "2000s hip-hop beat with rap vocals and punchy drums",
            "2010s EDM": "modern EDM with heavy bass and electronic drops"
        }

        prompt = lyrics + " in the style of " + style_map[decade] if input_type == "Lyrics" else style_map[decade]

        if input_type == "Melody (Upload WAV)" and uploaded_file:
            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                tmp.write(uploaded_file.read())
                wav_path = tmp.name
                wav, sr = torchaudio.load(wav_path)
                wav = wav[None, :]

            model.set_generation_params(duration=4)
            output = model.generate_with_chroma([prompt], wav, sr)
        else:
            model.set_generation_params(duration=4)
            output = model.generate([prompt])

        # Save audio output
        output_path = "generated_output.wav"
        torchaudio.save(output_path, output[0], 32000)

        st.success("✅ Done! Enjoy your time-traveling music 🎧")
        st.audio(output_path)

# Footer
st.markdown('<div class="footer">Made with ❤️ by MusicGen & Streamlit</div>', unsafe_allow_html=True)
