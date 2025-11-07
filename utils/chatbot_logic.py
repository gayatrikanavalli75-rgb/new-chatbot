# chatbot_logic.py
import google.generativeai as genai
# import os # You might need this later

# Replace 'YOUR_API_KEY' with your actual key (or use os.getenv() for security)
genai.configure(api_key="AIzaSyCTdZruTTEs_2ZRSQZSU782e2GBUUArmoE")

# Define the system instruction for the chatbot
system_instruction = "You are a friendly and helpful Student Admission Chatbot for 'XYZ University'. Your responses must be concise, professional, and directly address student inquiries about admission requirements, deadlines, and courses. If a question is outside the scope of admissions, politely suggest they contact the main administration office."
model_name = "gemini-2.5-flash" # The corrected model name

def get_bot_response(user_message):
    try:
        model = genai.GenerativeModel(
            model_name=model_name,
            system_instruction=system_instruction
        )
        
        response = model.generate_content(user_message)
        
        # Check if the response was blocked by safety settings
        if response.candidates and response.candidates[0].finish_reason.name == "SAFETY":
             # This will show the user why it was blocked
             return "I'm sorry, I cannot respond to that query due to safety guidelines. Please ask an admissions-related question."
        
        return response.text
        
    except Exception as e:
        # ⚠️ CRITICAL CHANGE: Return the actual error message for diagnosis
        error_message = f"AI Service Error: {type(e).__name__}: {str(e)}"
        print(error_message) # Still print to console/log
        return error_message # Return the detailed error to the UI