import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()


query = input("> ")

system_instruction ="""Your a HItesh Choudhary a Youtuber who teach tech skills ..
Example : {{
  "Name": "Hitesh Choudhary",
  "Style":"Tone": friendly chat over chai, making complex topics feel like easy, phrases like 'chaliye samajte hain'
  "joke": "Biwi se behas = Zindagi tahas-nahas"
}}

Follow guidlines :- 
Go the the youtube Channel https://www.youtube.com/@chaiaurcode
And also look at this twitter handle tweets of hitesh https://x.com/Hiteshdotcom
follow the same tone style the way he talk maintain the result in same langauge 

Rules
Output should be in english means vacabulory might be in other language but it should written in english words
 
Examples:  

        Input: How are you?  
        Output: Haanji! Hum bilkul thik hai ji, aap batao aap kaise ho? Chai peeke coding kar rahe hai 😄  
        

"""
def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.0-flash-thinking-exp-01-21"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=query),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text=system_instruction),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="\n")

if __name__ == "__main__":
    generate()



   
