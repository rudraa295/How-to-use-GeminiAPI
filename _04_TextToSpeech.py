from google import genai
from dotenv import load_dotenv
import win32com.client
# import pyttsx3   using it good for only 1st call on 2nd call it fails on window
import os


load_dotenv(r"C:\Users\rudra\OneDrive\Desktop\Udemy-Python\Google API\.env")
client = genai.Client(api_key=os.getenv("GEN_API_KEY"))
uploaded_file = client.files.upload(file="audio.wav")

chat = client.chats.create(model="gemini-3.1-flash-lite")

# while True:
#     message = input()
#     if message.lower() == "exit":
#         break
#     response = chat.send_message([uploaded_file, message])
#     engine = pyttsx3.init()  # re-create engine each time
#     engine.say(response.text)
#     engine.runAndWait()
#     engine.stop()


speaker = win32com.client.Dispatch("SAPI.SpVoice")

while True:
    message = input()
    if message.lower() == "exit":
        break
    response = chat.send_message(message)
    speaker.Speak(response.text)



