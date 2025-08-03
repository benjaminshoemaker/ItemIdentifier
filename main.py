from flask import Flask, render_template, request
import requests
import base64
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    image = request.files['image']
    image_content = base64.b64encode(image.read()).decode('utf-8')

    api_key = os.environ['GOOGLE_VISION_API_KEY']
    url = f'https://vision.googleapis.com/v1/images:annotate?key={api_key}'

    body = {
        "requests": [{
            "image": {
                "content": image_content
            },
            "features": [
                { "type": "LABEL_DETECTION", "maxResults": 3 },
                { "type": "WEB_DETECTION", "maxResults": 5 }
            ]
        }]
    }

    response = requests.post(url, json=body)
    data = response.json()

    label = "Unknown"

    try:
        # Try to use WEB_DETECTION result first (bestGuessLabel)
        web_detection = data['responses'][0].get('webDetection', {})
        if 'bestGuessLabels' in web_detection and len(web_detection['bestGuessLabels']) > 0:
            label = web_detection['bestGuessLabels'][0]['label']
        # Fallback to LABEL_DETECTION if needed
        elif 'labelAnnotations' in data['responses'][0]:
            label = data['responses'][0]['labelAnnotations'][0]['description']
    except Exception as e:
        print("Error parsing label:", e)

    return render_template('result.html', label=label)

if __name__ == '__main__':
    app.run(debug=True)
