from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()



client = genai.Client(api_key='GEMINI_API_KEY')

response = client.models.generate_content(
    model= '',
    contents = '',

)
print(response.text)