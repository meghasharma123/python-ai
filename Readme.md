# Basics

1. Python is `dynamic type` language.
2. Naming convention is usually `snake case` i.e. separated by _ (underscore).
3. The `range()` function in Python generates an immutable sequence of integers, most commonly used to control the execution count of for loops.
   1. range(stop)
   2. range(start, stop)
   3. range(start, stop, step)
4. A `list` in Python is a built-in, ordered, mutable (changeable), and zero-indexed collection that allows you to store multiple items in a single variable. Lists can hold duplicate items and elements of different data types simultaneously.
5. A `dictionary` in Python is a built-in data structure used to store data in key-value pairs. [like an hashmap]
6. A `tuple` is a built-in collection data type used to store an ordered, immutable sequence of elements. Unlike lists, once a tuple is created, its values cannot be added, removed, or changed.

# Functions

- reusable blocks of code designed to perform a specific task.
- Argument Types
  - Default Arguments [power(4) -> def power(base, exponent=2):]
  - Keyword Arguments [describe_pet(name="Buddy", animal="dog") -> def describe_pet(animal, name)]
  - Arbitrary Arguments (*args and **kwargs): `When you don't know beforehand how many arguments a user might pass`
    - *args: Receives a tuple of positional arguments.
    - **kwargs: Receives a dictionary of keyword arguments.


# Classes

- In Python, a class is a blueprint or template for creating objects. It bundles data (attributes) and behavior (methods) together into a single package, allowing you to write structured and reusable object-oriented code.

```
class Dog:
    species = "Canine"  # Class variable

    def __init__(self, name, breed):
        self.name = name    # Instance variable (unique to each dog)
        self.breed = breed  # Instance variable

# Creating distinct objects with unique data
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Rex", "German Shepherd")
```

# LLM

- Large Language Models (LLMs) are machine learning models trained on vast amount of textual data to generate and understand human-like language. These models can perform a wide range of natural language processing tasks from text generation to sentiment analysis and summarisation.

- **An LLM has no memory.** Every time you call it, it's a completely blank slate. It does *not* remember your previous message.

- stateful model - we user AI server memory

```
global previous_id
try:
  response = client.interactions.create(
    model="gemini-2.5-flash",
    input=user_message,
    previous_interaction_id=previous_id
  )

  previous_id = response.id

  return response.output_text
```

- stateless model - we use a list or dictonary to store data and then send it to the agent everytime.

```
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
```


# Error handling

`try`: Runs the risky code that might cause an error.
`except`: Catches and handles the error if one occurs.
`else`: Executes only if no exception occurs in try.
`finally`: Runs regardless of what happens useful for cleanup tasks like closing files.

```
try:
    n = 0
    res = 100 / n
    
except ZeroDivisionError:
    print("You can't divide by zero!")
    
except ValueError:
    print("Enter a valid number!")
    
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")
```

