from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
agentmd=open("Agent.md", "r").read()
skill_newsmd=open("SKILL_news.md", "r").read()
skill_weathermd=open("SKILL_weather.md", "r").read()
messages = [{"role": "system", "content": agentmd + skill_newsmd + skill_weathermd}]
while True:
    user_input=input("Enter your message: ")
    messages.append({"role": "user", "content": user_input})
    while True:
        print("------------[Agent] loop start-----------")
        response = client.chat.completions.create(model="gpt-5.4",messages=messages,)
        messages.append({"role": "assistant", "content": response.choices[0].message.content})     
        if response.choices[0].message.content.startswith("complete: "):
            print("------------[Agent] loop end-----------")
            print(response.choices[0].message.content)
            break
        # extract the code to execute
        command = response.choices[0].message.content[len("command: "):]
        print(f"[Agent] Need to excute command: {command}")
        command_result = os.popen(command).read()
        content=f"excution complete:\n{command_result}"
        messages.append({"role": "user", "content": content})
