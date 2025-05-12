

from fer import FER
import cv2
import spotipy
from spotipy.oauth2 import SpotifyOAuth

emotion_to_mood = {
    "happy": "upbeat",
    "sad": "calm",
    "angry": "intense",
    "neutral": "chill",
    "fear": "soothing",
    "surprise": "pop",
    "disgust": "dark"
}

def get_emotion_and_mood():
    detector = FER(mtcnn=True)
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        raise Exception("Couldn't read from webcam.")

    top_emotion = detector.top_emotion(frame)
    if not top_emotion:
        raise Exception("No emotion detected.")

    emotion, confidence = top_emotion
    mood = emotion_to_mood.get(emotion, "chill")
    return emotion, mood

def get_spotify_tracks(mood):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id="02cb21119a84438a826aaedde8d1063d",
        client_secret="6fe414627df54f97a8230afacd82dcdf",
        redirect_uri="http://localhost:8888/callback",
        scope="user-read-private"
    ))

    results = sp.search(q=mood, type='track', limit=3)
    tracks = []
    for track in results['tracks']['items']:
        tracks.append({
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'url': track['external_urls']['spotify']
        })
    return tracks
