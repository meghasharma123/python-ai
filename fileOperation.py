from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

with open("file.txt", "r", encoding="utf-8") as f:
    document = f.read()

prompt = f"""
Here is a meeting transcript:
{document}

Extract the action items.
"""

try:
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=document
    )
    summary=response.text
except Exception as e:
    summary = f"Something went wrong: {e}"

print(summary)

with open("summary.txt","w",encoding="utf-8") as f:
    f.write(summary)

