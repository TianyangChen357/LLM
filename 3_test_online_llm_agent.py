from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
messages = [{"role": "system", "content": '''
             You are a helpful assistant. You need follow the following format when answering questions:
             1. if you think you need to excute some shell script to get the answer, 
             you should output 'command: <code>', code is the code to excute. Do not give further explanations as I want my orchestration layer to decide how to execute the code and when to execute the code. 
             2. if you think you do not need to excute code, you can output 'complete: 'XXX'', XXX is the answer to the question.
             '''}]
while True:
    user_input=input("Enter your message: ")
    messages.append({"role": "user", "content": user_input})
    while True:
        print("------------[Agent] loop start-----------")
        response = client.chat.completions.create(
            model="gpt-4o",  # OpenAI's GPT-4o model
            messages=messages,
        )
        messages.append({"role": "assistant", "content": response.choices[0].message.content})

        
        if response.choices[0].message.content.startswith("complete: "):
            print("------------[Agent] loop end-----------")
            print(response.choices[0].message.content)
            break
        # extract the code to execute
        command = response.choices[0].message.content[len("command: "):]
        print(f"[Agent] Need to excute command: {command}")
        # excute the code and get the result
        command_result = os.popen(command).read()
        content=f"excution complete:\n{command_result}"
        print(f"[Agent] {content}")
        messages.append({"role": "user", "content": content})
