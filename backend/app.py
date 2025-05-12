from flask import Flask, jsonify, render_template
from detectFaceEmotion import get_emotion_and_mood, get_spotify_tracks

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['GET'])
def detect():
    try:
        emotion, mood = get_emotion_and_mood()
        tracks = get_spotify_tracks(mood)
        return jsonify({
            'emotion': emotion,
            'mood': mood,
            'tracks': tracks
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
