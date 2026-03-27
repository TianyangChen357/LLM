from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
messages = [{"role": "system", "content": open("Agent.md", "r").read()}]
while True:
    user_input=input("Enter your message: ")
    messages.append({"role": "user", "content": user_input})
    while True:
        response = client.chat.completions.create(model="gpt-4o",messages=messages,)
        messages.append({"role": "assistant", "content": response.choices[0].message.content})     
        if response.choices[0].message.content.startswith("complete: "):
            print(response.choices[0].message.content)
            break

        command = response.choices[0].message.content[len("command: "):]
        command_result = os.popen(command).read()
        content=f"excution complete:\n{command_result}"
        messages.append({"role": "user", "content": content})
