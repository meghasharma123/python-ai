from fastapi import FastAPI
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel

load_dotenv()
client = genai.Client()

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"Hello world."}

class Review(BaseModel):
    txt: str

class Sentiment(BaseModel):
    label:str
    score:str
    
@app.post("/sentiment")
def sentimentAnalysis(review:Review):
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=(
            "Find the sentiment of this customer review. "
            "label must be 'positive', 'negative', or 'neutral'. "
            "score must be a number from 1 (very bad) to 5 (very good). "
            f"Review: {review.txt}"
        ),
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=Sentiment
        )
    )

    return response.parsed

