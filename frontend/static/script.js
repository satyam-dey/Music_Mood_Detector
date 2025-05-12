function detectMood() {
  const resultDiv = document.getElementById('result');
  resultDiv.innerHTML = "🎥 Detecting your mood...";

  fetch('/detect', { method: 'GET' })
    .then(response => response.json())
    .then(data => {
      if (data.error) {
        resultDiv.innerHTML = `<p>⚠️ ${data.error}</p>`;
      } else {
        const { emotion, mood, tracks } = data;

        let output = `
          <h2>😄 Detected Emotion: ${emotion}</h2>
          <h3>🎶 Recommended Mood: ${mood}</h3>
          <ul>
        `;

        tracks.forEach((track, index) => {
          output += `<li>${index + 1}. <a href="${track.url}" target="_blank">${track.name}</a> by ${track.artist}</li>`;
        });

        output += '</ul>';
        resultDiv.innerHTML = output;
      }
    })
    .catch(error => {
      resultDiv.innerHTML = `<p>❌ Failed to detect mood: ${error}</p>`;
    });
}
