from dotenv import load_dotenv
load_dotenv()

# env key -> GOOGLE_API_KEY
from google import genai

client = genai.Client()

response = client.interactions.create(
    model="gemini-3.5-flash",
    input="Tell me who invented chole bhature in 1 line"
)

print(response.output_text)


def generate_recipe(ingradients, cuisine, diet):
  
    prompt = f'''
        Generate one food receipe using these ingradients: {','.join(ingradients)}
        Receipe should not be more than 100 words
        Cuisine: {cuisine}
        Diet: {diet}
    '''
    response = client.interactions.create(
        model="gemini-3.5-flash",
        input=prompt
    )

    return response.output_text

recipe = generate_recipe(["Tomatoes", "lentils", "onion", "jeera", "salt"],"Indian","Vegan")
print(recipe)