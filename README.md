# 🍳 CloudCook: The Self-Healing Meal Planning Agent

CloudCook is a resilient, terminal-based AI concierge designed to solve the "what's for dinner?" dilemma.

Unlike traditional recipe apps that search static databases, CloudCook leverages the generative power of **Google's Gemini LLM** to act as an improvisational chef. You simply provide a natural language list of raw ingredients (e.g., *"chicken, leftover rice, and a tomato"*), and the agent instantaneously synthesizes a unique, step-by-step recipe.

## 🌟 Key Features

* **🛡️ "Self-Healing" Model Diagnostics:** The agent automatically scans your Google account for available Gemini models (Flash, Pro, Experimental) and routes traffic to a working one. This prevents crashes due to model deprecation or quota limits.
* **🗣️ Natural Language Interface:** No complex search filters. Just type your ingredients in plain English.
* **🔄 Robust Resilience:** Integrated retry logic handles API hiccups so you always get a response.

## 🛠️ Installation & Setup

1.  **Get an API Key**
    * Visit [Google AI Studio](https://aistudio.google.com/) and create a free API Key.

2.  **Install Dependencies**
    You need Python installed. Then run:
    ```bash
    pip install google-generativeai
    ```

3.  **Configure the Agent**
    * Open `cloudcook.py`.
    * Find the line `GEMINI_API_KEY = "PASTE_YOUR_KEY_HERE"`.
    * Paste your API key inside the quotes.

## 🚀 How to Run

Simply run the script in your terminal:

```bash
python cloudcook.py

🔧 Tech Stack

Language: Python 3
AI Engine: Google Gemini API (google-generativeai)
Logic: Dynamic Model Selection & Error Handling
