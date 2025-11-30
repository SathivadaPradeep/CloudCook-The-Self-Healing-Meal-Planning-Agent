import google.generativeai as genai
import time

# ==========================================
# PASTE YOUR NEW KEY INSIDE THE QUOTES
GEMINI_API_KEY = "PASTE_YOUR_KEY_HERE"
# ==========================================

genai.configure(api_key=GEMINI_API_KEY)

def find_and_run():
    print("\n🔍 SCANNING for a working, free brain...")
    
    working_model = None

    # Get the official list from Google
    try:
        for m in genai.list_models():
            # Only look for text generation models
            if 'generateContent' in m.supported_generation_methods:
                print(f"   Testing: {m.name}...", end=" ")
                
                try:
                    # Try to use it
                    test_model = genai.GenerativeModel(m.name)
                    test_model.generate_content("Hello")
                    print("✅ WINNER!")
                    working_model = test_model
                    break # We found it! Stop looking.
                except Exception as e:
                    # If it's a Quota error (429) or Not Found (404), skip it
                    print("❌")
                    
    except Exception as e:
        print(f"\n❌ Error listing models: {e}")

    # Did we find one?
    if working_model:
        print("\n" + "="*50)
        print(f"🍳 CloudCook Agent is Online! (Using {working_model.model_name})")
        print("="*50)
        
        while True:
            user_input = input("\nWhat ingredients do you have? (or 'quit'): ")
            if user_input.lower() in ['quit', 'exit']: break
            
            print(f"Thinking...")
            try:
                response = working_model.generate_content(f"Suggest 1 simple recipe for: {user_input}")
                print("-" * 40)
                print(response.text)
                print("-" * 40)
            except:
                print("Error generating recipe.")
    else:
        print("\n❌ CRITICAL: No free models worked.")

if __name__ == "__main__":
    find_and_run()