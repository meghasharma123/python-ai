from google import genai
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from google.genai import types

load_dotenv()
client = genai.Client()

app = FastAPI()

class Review(BaseModel):
    txt: str

class Sentiment(BaseModel):
    label: str   # "positive", "negative", or "neutral"
    score: int   # 1 (very bad) to 5 (very good)
    theme: str


@app.post("/analyze")
def analyze(review:Review):
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=(
            "Analyze this customer review.\n"
            "1. label must be 'positive', 'negative', or 'neutral'.\n"
            "2. score must be a number from 1 (very bad) to 5 (very good).\n"
            "3. theme must be ONE lowercase word for the main topic "
            "(for example: delivery, taste, price, service, quality).\n"
            f"Review: {review.txt}"
        ),
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=Sentiment,
        )
    )

    return response.parsed

