from google import genai
from dotenv import load_dotenv
import os

load_dotenv(r"C:\Users\rudra\OneDrive\Desktop\Udemy-Python\Google API\.env")
client = genai.Client(api_key=os.getenv("GEN_API_KEY"))
# response = client.models.generate_content(
#     model="gemini-3.1-flash-lite",
#     contents = "What is the capital of France in one word?")
# print(response.text)

#for stream reply we can use
response = client.models.generate_content_stream(
    model="gemini-3.1-flash-lite",
    contents = "What is the capital of France in 100 word?")
for i in response:
    print(i.text)

