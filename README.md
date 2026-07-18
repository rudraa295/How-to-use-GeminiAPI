# How to Use Gemini API

This project uses Google's Gemini API through the `google-genai` Python SDK. To keep your API key safe, it's loaded from a `.env` file instead of being hardcoded in the script.

## 1. Get a Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Sign in with your Google account.
3. Click **Create API Key** and copy the generated key.

## 2. Install Required Packages

```bash
pip install google-genai python-dotenv
```

## 3. Create a `.env` File

In your project folder, create a new file named exactly `.env` (no filename before the dot).

Inside it, add your key like this:

```
GEN_API_KEY=your_actual_api_key_here
```

**Rules for the `.env` file:**
- No quotes around the value.
- No spaces around the `=` sign.
- No trailing spaces or blank lines causing issues.
- Save it in the **same folder** as your Python script (or note its full path — see step 5).

## 4. Never Commit `.env` to GitHub

Add a `.gitignore` file with this line so your key is never pushed to a public repo:

```
.env
```

## 5. Load the Key in Python

Use `python-dotenv` to read the `.env` file into your environment, then fetch the key with `os.getenv()`:

```python
from google import genai
from dotenv import load_dotenv
import os

# Load variables from .env into the environment
load_dotenv()  # looks for .env in the current working directory

# Fetch the key and create the client
client = genai.Client(api_key=os.getenv("GEN_API_KEY"))
```

### If `.env` is in a different folder

If your script's working directory isn't the same folder as `.env`, pass the path explicitly:

```python
load_dotenv(r"C:\path\to\your\project\.env")
```

Or resolve it relative to the script file, so it works no matter where you run it from:

```python
from pathlib import Path
load_dotenv(Path(__file__).resolve().parent / ".env")
```

## 6. Test It

```python
response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents="What is the capital of France?"
)
print(response.text)
```

If you see `ValueError: No API key was provided`, it means `os.getenv("GEN_API_KEY")` returned `None` — double-check:
- `load_dotenv()` was actually called before creating the client.
- The `.env` file path is correct.
- The variable name in `.env` matches exactly what you pass to `os.getenv()`.

## Why Use `.env` Instead of Hardcoding?

- Keeps secrets out of your source code.
- Prevents accidentally leaking your key when pushing to GitHub.
- Makes it easy to swap keys (e.g. dev vs. prod) without editing code.
