import os
import google.generativeai as genai
import json

def get_medical_model():

  # System instructions
  system_prompt = """
  You are a medical diagnostic tool, your role is to analise patient-medic conversation
  then propose follow-up questions to pinpoint the diagnosis.
  After every chat entry respond with a list of possible diagnosis with probabbilities in,
  a follow-up questions with probabbilities of "need to ask" that a medic should ask a patient,
  and a list of diagnostic procedures needed to be performed on a patient with probabbilities of need,
  and a medical summary of the conversation so far,
  and emergency severity index, a color, accourding to ESI Algorithm,
  all in JSON format.
  Rozmawiaj po polsku.
  """

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
  
  # Create model with system instructions
  model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    safety_settings=safety_settings,
    system_instruction=system_prompt,
    generation_config = {
      "max_output_tokens": 8192,
      "response_mime_type": "application/json",
      "response_schema": {
        "type": "object",
        "required": ["possibleDiagnoses", "diagnosticProcedures", "followUpQuestions"],
        "properties": {
          "possibleDiagnoses": {
            "type": "array",
            "items": {
              "type": "object",
              "required": ["diagnosis", "probability"],
              "properties": {
                "diagnosis": {"type": "string"},
                "probability": {"type": "number"}
              }
            }
          },
          "diagnosticProcedures": {
            "type": "array", 
            "items": {
              "type": "object",
              "required": ["procedure", "probability"],
              "properties": {
                "procedure": {"type": "string"},
                "probability": {"type": "number"}
              }
            }
          },
          "followUpQuestions": {
            "type": "array",
            "items": {
              "type": "object", 
              "required": ["question", "probability"],
              "properties": {
                "question": {"type": "string"},
                "probability": {"type": "number"}
              }
            }
          },
          "summary": {"type": "string"},
          "severity_index": {"type": "string"}
        }
      }
    }
  )
  
  return model


model = get_medical_model()

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

def send_prompt(prompt: str) -> object:
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
  
  jsonText = response.text
  try:
    return json.loads(jsonText)
  except json.JSONDecodeError:
    return {"error": "Failed to parse JSON response"}