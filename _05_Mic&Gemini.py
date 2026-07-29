from google import genai
from dotenv import load_dotenv
import win32com.client
import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
import os

# ---- Setup ----
load_dotenv(r"C:\Users\rudra\OneDrive\Desktop\Udemy-Python\Google API\.env")
client = genai.Client(api_key=os.getenv("GEN_API_KEY"))
chat = client.chats.create(model="gemini-3.1-flash-lite")

speaker = win32com.client.Dispatch("SAPI.SpVoice")
recognizer = sr.Recognizer()

fs = 44100          # sample rate
duration = 5        # seconds to record each turn
mic_file = "mic_input.wav"


def record_audio():
    print("\n🎙️ Listening... speak now")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    write(mic_file, fs, recording)


def transcribe_audio():
    with sr.AudioFile(mic_file) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        print("Speech service error:", e)
        return None


# ---- Main loop ----
while True:
    record_audio()
    message = transcribe_audio()

    if message is None:
        print("Didn't catch that, try again.")
        continue

    print("You said:", message)

    if message.lower() == "exit":
        break

    response = chat.send_message(message)
    print("Gemini:", response.text)

    if response.text:
        speaker.Speak(response.text)