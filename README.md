# 👗 Virtual Fitting Room: AI-Powered Try-On with Gemini 2.5 Flash Image
## 📌 Overview

This project demonstrates how to use Google’s Gemini 2.5 Flash Image model to create an AI-powered virtual fitting room. By combining a person’s photo, an outfit image, and a text prompt, the system generates a realistic try-on result where the person appears to be wearing the chosen outfit.

This project is built for the Kaggle Gemini 2.5 Flash Image Challenge.

## 🚀 Features

Upload a person photo and outfit photo

Use Gemini’s multimodal image generation to blend them

Generate photorealistic try-on results in seconds

Error handling for prohibited or unsupported prompts

Supports different outfits: wedding dresses, swimsuits, shirts, pants, etc.

## 🛠️ Tech Stack

Python 3.10+

Google Generative AI (Gemini API)

PIL (Pillow) for image processing

io.BytesIO for handling binary image responses

## 📂 Project Structure
```
.
├── dress.jpg
├── model.jpg
├── fitAura.py        # main script
```

## ⚙️ Setup Instructions

Clone the Repository
```
git clone https://github.com/your-username/virtual-fitting-room.git
cd virtual-fitting-room
```

Optional: Create & Activate Virtual Environment
```
python -m venv venv
source venv/bin/activate   # on macOS/Linux
venv\Scripts\activate      # on Windows
```

Install api key into your machine
Gemini api key can be found here: https://aistudio.google.com/apikey
```
setx GEMINI_API_KEY "your_gemini_api_key_here"
```

Install Dependencies
```
# Install the main SDK
pip install -U google-genai

# We also recommend Pillow for handling images
pip install Pillow
```

google-generativeai
pillow


Set API Key
Replace the placeholder with your Gemini API key inside main.py:
```
client = genai.Client(api_key="YOUR_API_KEY_HERE")
```

Run the Script
```
python fitAura.py
```

Generated try-on results will be saved as:

photo_YYYY-MM-DD.jpg

## 🎥 Demo

Video: [YouTube Link Here]

Kaggle Writeup: (https://www.kaggle.com/competitions/banana/writeups/ai-powered-virtual-fitting-room)

## 🌍 Use Cases

Fashion e-commerce – Virtual fitting rooms to reduce product returns

Styling apps – Try different outfits instantly

Creative projects – Blending fashion + AI-generated visuals

## 📜 License

MIT License – free to use, modify, and distribute.
