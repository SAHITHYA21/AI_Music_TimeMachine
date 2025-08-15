import streamlit as st
import torchaudio
from audiocraft.models import MusicGen
from audiocraft.utils.notebook import display_audio
import tempfile

# Load model (Melody or Text-to-Music)
model = MusicGen.get_pretrained('melody')

st.title("🎼 AI Music Time Machine")
st.markdown("Convert lyrics or a melody into music from another decade!")

# Inputs
input_type = st.radio("Input Type", ["Lyrics", "Melody (Upload WAV)"])
decade = st.selectbox("Choose a Decade Style", ["1920s Jazz", "1980s Synthwave", "2000s Hip-Hop", "2010s EDM"])

if input_type == "Lyrics":
    lyrics = st.text_area("Enter Lyrics or Prompt")

if input_type == "Melody (Upload WAV)":
    uploaded_file = st.file_uploader("Upload melody file (WAV format)", type=["wav"])

# Generate Button
if st.button("🕰️ Time Travel! Generate Music"):
    with st.spinner("Generating music..."):

        # Prepare decade-style prompt
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

        st.audio(output_path)
        st.success("Done!")

