from google import genai
from dotenv import load_dotenv
import os

load_dotenv(r"C:\Users\rudra\OneDrive\Desktop\Udemy-Python\Google API\.env")
client = genai.Client(api_key=os.getenv("GEN_API_KEY"))

chat = client.chats.create(model="gemini-3.1-flash-lite")

while True:
    message = input()
    if message.lower() == "quit":
        break
    message = chat.send_message_stream(message)
    for i in message:
        print(i.text)

