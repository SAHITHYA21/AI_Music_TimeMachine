# 🎼 AI Music Time Machine

**AI Music Time Machine** is a fun and creative web app built using **Streamlit** and **Meta’s MusicGen** model. It lets users generate music in styles from different decades using either **lyrics** or a **melody (WAV file)** as input.

---

## 🌟 Features

- 🎤 Convert **lyrics** into decade-styled music
- 🎵 Upload a **melody (WAV file)** and transform it
- 🕰️ Choose styles like:
  - 1920s Jazz
  - 1980s Synthwave
  - 2000s Hip-Hop
  - 2010s EDM
- 🚀 Real-time music generation with Meta’s **MusicGen**
- 🎧 Listen to the output directly in the browser

---

## 📦 Requirements

Make sure you have the following Python packages installed:
- streamlit
- torch==1.13.1
- torchaudio==0.13.1
- audiocraft

> ⚠️ Some packages may require additional system-level dependencies (e.g., `ffmpeg` for audio support). It’s recommended to use a virtual environment.

---

## 🛠️ Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI_Music_TimeMachine.git
cd AI_Music_TimeMachine
```

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app.py
```


### Then open your browser to:

http://localhost:8501

---

## 📁 Project Structure

```
AI_Music_TimeMachine/
│
├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── generated_output.wav # (Created during runtime)
```

---

## 🎓 Example Usage

Input:
"A funky beat with smooth flow in the style of 2000s Hip-Hop"

Output:
🔊 Audio generated with MusicGen, downloadable and playable in-browser

Screenshot of Application:
![Application screenshot](https://github.com/SAHITHYA21/AI_Music_TimeMachine/blob/main/app_screenshot.png)

---

## 🙌 Acknowledgments

- Meta’s MusicGen (Audiocraft)
- Streamlit
- Inspired by the idea of blending AI + Music + Nostalgia 🎶🕰️
