# Clario - Gemini Streamlit Chatbot

A minimal Streamlit chatbot powered by Google Gemini via LangChain.

## Features
- Streamlit UI with a single input field
- LangChain ChatGoogleGenerativeAI integration
- Loads API key from .env
- Graceful handling of quota errors

## Getting Started

### 1) Create and activate a virtual environment (recommended)
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Configure environment variables
Copy the example and fill in your key:
```bash
cp .env.example .env
```
Edit .env and set:
```
GOOGLE_API_KEY=your_api_key_here
```

### 4) Run the app
```bash
streamlit run gemini_app3_streamlit.py
```

## Environment Variables
- GOOGLE_API_KEY: Your Google Generative AI API key.

## Notes
- .gitignore excludes common secrets like .env and service_account.json.
- If you see a quota error, check billing/quota or retry later.
