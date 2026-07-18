from google import genai
from dotenv import load_dotenv
import os

load_dotenv(r"C:\Users\rudra\OneDrive\Desktop\Udemy-Python\Google API\.env")
client = genai.Client(api_key=os.getenv("GEN_API_KEY"))
uploaded_file = client.files.upload(file="audio.wav")

chat = client.chats.create(model="gemini-3.1-flash-lite")

while True:
    message = input()
    if message.lower() == "quit":
        break
    response = chat.send_message_stream([uploaded_file, message])
    for chunk in response:
        print(chunk.text)