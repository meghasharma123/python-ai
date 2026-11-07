from google import genai
from pydantic import BaseModel
from google.genai import types

from dotenv import load_dotenv
load_dotenv()

client = genai.Client()

# This class IS the shape we want back. Note the types: str, int, list of str.
class Recipe(BaseModel):
    title: str
    ingredients: list[str]
    calories: int
    prep_time_minutes: int

# response = client.models.generate_content(
#     model="gemini-3.5-flash",
#     contents="Give me a simple Indian dal recipe.",
#     config=types.GenerateContentConfig(
#         response_mime_type="application/json",   # "reply in JSON"
#         response_schema=Recipe,                   # "...in exactly THIS shape"
#     ),
# )

# print(response.text) 

# exercise

class ReviewAnalysis(BaseModel):
    sentiment: str
    rating: int
    pros: list[str]
    cons: list[str]

response_schema = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="I ordered the wireless earbuds last week. Sound quality is amazing and battery lasts all day, but the case feels cheap and it arrived two days late. Probably won't buy from this brand again.",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",   # "reply in JSON"
        response_schema=ReviewAnalysis,                   # "...in exactly THIS shape"
    ),
)

print(response_schema.text) 
