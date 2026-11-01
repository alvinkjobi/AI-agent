from openai import OpenAI
from dotenv import load_dotenv
import os

# Load configuration from the .env file
load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)
messages=[]
print("*"*40)
print("\t My Ai Agent")
print("*"*40)

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chat. Goodbye!")
        break
    else:
        messages.append({
            "role": "user",
            "content": user_input
        })
        response = client.chat.completions.create(
            model=os.getenv("MODEL"),
            messages=messages
        )
        messages.append({
            "role": "assistant",
            "content": response.choices[0].message.content
        })

        '''for message in messages:
            print(f"{message['role'].capitalize()}: {message['content']}")'''
    
        print("AI: ", response.choices[0].message.content)
