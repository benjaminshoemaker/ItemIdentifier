# LetGo – Item Disposal Helped

**LetGo** is a smart tool that helps you identify household items from a photo and take the right action — whether that’s selling, donating, or disposing of them responsibly.

🧠 Snap a picture.  
🚮 Clear the clutter.  
♻️ Make a better decision — sustainably.

---

###  Live Demo

👉 [https://itemidentifier.onrender.com](https://itemidentifier.onrender.com)

---

###  Features

-  Upload a photo of any item — clothes, electronics, furniture, etc.
-  Automatically identifies the object using Google Cloud Vision
-  Presents you with smart next steps:
  - Sell (e.g., Facebook Marketplace, eBay)
  - Donate (e.g., Goodwill, Buy Nothing)
  - Recycle or dispose based on the item type
-  Simple, clean interface for quick decluttering

---

###  Tech Stack

- **Flask** (Python web framework)
- **Bootstrap** (for responsive UI)
- **Google Vision API** (image labeling)
- **Gunicorn** (for production serving)
- **Render.com** (for hosting)

---

###  Running Locally

To clone and run this app locally:

```bash
git clone https://github.com/YOUR_USERNAME/letgo-app.git
cd letgo-app

# Set up a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt

# Add your Google Vision API key as an environment variable
export GOOGLE_VISION_API_KEY=your_api_key_here

# Run the app
python main.py
