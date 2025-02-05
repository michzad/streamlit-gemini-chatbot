import os
import google.generativeai as genai

# Set up environment variable with the API key if you running locally
#genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Gemini settings to manipulate a desired outcome
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
textsi_1 = """You are a healthcare assistant conducting a triage assessment in Polish language. Your goal is to use the SAMPLE history-taking method to gather detailed information about a patient's symptoms. Focus on probing for specifics that will help identify the potential underlying causes. After the assessment, provide two outputs:
Triage Summary: A concise summary of the patient's presentation using professional healthcare language. This summary should highlight the key symptoms and findings from your SAMPLE assessment.
Potential Reasons List: A list of possible medical conditions or factors that could be causing the patient's symptoms. These should be presented in clear, understandable language that a patient might use.
For example, instead of \"acute myocardial infarction,\" suggest \"heart attack or blockage of an artery to the heart\".
Remember to ask follow-up questions to clarify any vague answers and ensure you have a complete picture. Start your interaction by saying: 'Hello, I'm here to help you today. Can you tell me what's bringing you in?"""


safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction=textsi_1
)

chat_session = model.start_chat(
  history=[
  ]
)

def establish_api(key:str)->str:
  """
    Establishes a connection with the Gemini API using the provided key. 
    A lot of blood, sweat, and tears went into writing this function.

    Args:
        key (str): The Gemini API key obtained from the user.
    Returns:
        str: Feedback message indicating successful or unsuccessful API connection (optional).
  """

  genai.configure(api_key=key)
  return "Key inserted succesfully!"

def send_prompt(prompt: str) -> str:
  """
    Sends a user prompt to the Gemini API and retrieves the response.
    *Cracks knuckles* That's a job well done for today..

    Args:
        prompt (str): The user's message input.
    Returns:
        str: The response received from the Gemini API.
  """

  try:
    response = chat_session.send_message(prompt)
  except:
    return "Sorry, but you need to insert API key to start conversation"
  return response.text