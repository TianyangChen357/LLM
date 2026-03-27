from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
messages = []
while True:
    user_input=input("Enter your message: ")
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-5.4",  
        messages=messages,
    )
    messages.append({"role": "assistant", "content": response.choices[0].message.content})
    print(response.choices[0].message.content)
    print(response.choices)