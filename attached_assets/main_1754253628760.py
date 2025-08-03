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
            "features": [{
                "type": "LABEL_DETECTION",
                "maxResults": 1
            }]
        }]
    }

    response = requests.post(url, json=body)
    label = "Unknown"
    try:
        label = response.json()['responses'][0]['labelAnnotations'][0]['description']
    except Exception as e:
        print("Error parsing label:", e)

    return render_template('result.html', label=label)

if __name__ == '__main__':
    app.run(debug=True)
