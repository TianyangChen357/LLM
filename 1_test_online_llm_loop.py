from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


while True:
    # Use OpenAI API directly
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    user_input=input("Enter your message: ")
    response = client.chat.completions.create(
        model="gpt-4o",  # OpenAI's GPT-4o model
        messages=[
            {"role": "user", "content": user_input}
        ],
    )
    print(response.choices[0].message.content)