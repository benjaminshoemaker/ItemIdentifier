from flask import Flask, render_template, request, flash, redirect, url_for
import requests
import base64
import os
import logging

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        # Check if image file was uploaded
        if 'image' not in request.files:
            flash('No image file uploaded. Please select an image.', 'error')
            return redirect(url_for('index'))
        
        image = request.files['image']
        
        # Check if file was actually selected
        if image.filename == '':
            flash('No image file selected. Please choose an image.', 'error')
            return redirect(url_for('index'))
        
        # Validate file type
        allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'}
        file_extension = ''
        if image.filename and '.' in image.filename:
            file_extension = image.filename.rsplit('.', 1)[1].lower()
        
        if file_extension not in allowed_extensions:
            flash('Invalid file type. Please upload an image file (PNG, JPG, JPEG, GIF, BMP, WEBP).', 'error')
            return redirect(url_for('index'))
        
        # Read and encode image
        image_content = base64.b64encode(image.read()).decode('utf-8')
        
        # Get API key from environment
        api_key = os.getenv('GOOGLE_VISION_API_KEY')
        if not api_key:
            flash('Google Vision API key not configured. Please contact the administrator.', 'error')
            return redirect(url_for('index'))
        
        # Prepare API request
        url = f'https://vision.googleapis.com/v1/images:annotate?key={api_key}'
        
        body = {
            "requests": [{
                "image": {
                    "content": image_content
                },
                "features": [{
                    "type": "LABEL_DETECTION",
                    "maxResults": 5
                }]
            }]
        }
        
        # Make API request
        response = requests.post(url, json=body, timeout=30)
        
        if response.status_code != 200:
            app.logger.error(f"Google Vision API error: {response.status_code} - {response.text}")
            flash('Failed to analyze the image. Please try again later.', 'error')
            return redirect(url_for('index'))
        
        # Parse response
        result = response.json()
        
        if 'responses' not in result or not result['responses']:
            flash('No response from image analysis service. Please try again.', 'error')
            return redirect(url_for('index'))
        
        response_data = result['responses'][0]
        
        # Check for errors in the response
        if 'error' in response_data:
            app.logger.error(f"Google Vision API response error: {response_data['error']}")
            flash('Failed to analyze the image. The image might be corrupted or unsupported.', 'error')
            return redirect(url_for('index'))
        
        # Extract labels
        labels = []
        if 'labelAnnotations' in response_data and response_data['labelAnnotations']:
            labels = [label['description'] for label in response_data['labelAnnotations']]
        
        if not labels:
            flash('Could not identify any items in the image. Please try with a clearer image.', 'warning')
            return redirect(url_for('index'))
        
        primary_label = labels[0]
        
        return render_template('result.html', label=primary_label, all_labels=labels)
        
    except requests.RequestException as e:
        app.logger.error(f"Network error during API request: {str(e)}")
        flash('Network error occurred. Please check your internet connection and try again.', 'error')
        return redirect(url_for('index'))
    
    except Exception as e:
        app.logger.error(f"Unexpected error during image analysis: {str(e)}")
        flash('An unexpected error occurred. Please try again.', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    # Bind to 0.0.0.0 and port 5000 for external access
    app.run(host='0.0.0.0', port=5000, debug=True)
