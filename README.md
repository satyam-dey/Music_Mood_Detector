Here's a polished `README.md` file for your **Music Mood Detector** project:

# 🎵 Music Mood Detector AI/ML Project

This is a fun and interactive web application that uses **Facial Emotion Recognition** to detect your current mood using your webcam, then recommends **Spotify tracks** that match your emotion.

---

## 💡 Features

- 🎥 Real-time face emotion detection using webcam
- 🧠 AI/ML powered emotion recognition (FER with MTCNN)
- 🎧 Music mood mapping based on emotion
- 🔗 Spotify API integration to fetch mood-matching songs
- 🌐 Web frontend with HTML, CSS, and JavaScript
- 🐍 Flask backend to handle detection and API calls

---

## 📂 Project Structure

```

    MUSIC\_MOOD\_DETECTOR/
            ├── backend/
            │   ├── app.py                   # Flask backend
            │   └── detectFaceEmotion.py     # Emotion detection and Spotify integration
            ├── frontend/
            │   ├── templates/
            │   │   └── index.html           # Frontend UI
            │   └── static/
            │       ├── style.css            # CSS styling
            │       └── script.js            # Frontend JS logic
            └── README.md


## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/music-mood-detector.git
cd music-mood-detector
````

### 2. Create Virtual Environment & Install Requirements

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

> If there's no `requirements.txt`, install manually:

```bash
pip install fer opencv-python spotipy flask
```

---

## 🔐 Spotify Setup

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Create an App
3. Set the Redirect URI to: `http://localhost:8888/callback`
4. Copy your **Client ID** and **Client Secret**

Set them in `detectFaceEmotion.py` or as environment variables:

```bash
SPOTIPY_CLIENT_ID=your_id
SPOTIPY_CLIENT_SECRET=your_secret
SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
```

---

## 🚀 Run the App

```bash
cd backend
python app.py
```

Visit: [http://localhost:5000](http://localhost:5000)

Click the detect button — your webcam activates — emotion is detected — songs appear!

---

## 📸 Emojis & Music Moods Mapping

| Emotion     | Music Mood |
| ----------- | ---------- |
| 😊 Happy    | Upbeat     |
| 😢 Sad      | Calm       |
| 😠 Angry    | Intense    |
| 😐 Neutral  | Chill      |
| 😨 Fear     | Soothing   |
| 😮 Surprise | Pop        |
| 🤢 Disgust  | Dark       |

---

## 📦 Future Improvements

* Add live webcam feed in frontend
* Display album art and song preview
* Save emotion history
* Deploy online (Render/Heroku/Railway)

---

## 🧑‍💻 Author

Made with ❤️ by \Satyam Dey
📧 [satyamdey4651@gmail.com](mailto:satyamdey4651@gmail.com)
🔗 GitHub: [satyam-dey](https://github.com/satyam-dey)
