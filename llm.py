from dotenv import load_dotenv
load_dotenv()

# env key -> GOOGLE_API_KEY
from google import genai

client = genai.Client()

# response = client.interactions.create(
#     model="gemini-3.5-flash",
#     input="Tell me who invented chole bhature in 1 line"
# )

# print(response.output_text)


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

# recipe = generate_recipe(["Tomatoes", "lentils", "onion", "jeera", "salt"],"Indian","Vegan")
# print(recipe)

#stateless

conversation = []

def chat(user_message):
    conversation.append({
        "type": "user_input",
        "content": [
            {"type": "text", "text": user_message}
        ]
    })
  
    try:
        response = client.interactions.create(
            model="gemini-3.5-flash",
            input=conversation
        )
        reply = response.output_text
    except Exception as e:
        return f"Sorry, something went wrong: {e}"

    conversation.extend([
        step.model_dump(exclude_none=True)
        for step in response.steps
    ])
    return reply

# stateful 
previous_id = None

def chatState(user_message):
    global previous_id

    try:
        response = client.interactions.create(
            model="gemini-3.5-flash",
            input=user_message,
            previous_interaction_id=previous_id
        )

        previous_id = response.id

        return response.output_text

    except Exception as e:
        return f"Sorry, something went wrong: {e}"

print(chat("Hi! My name is Megha. Please remember it."))
print("---")
print(chat("What is my name?"))