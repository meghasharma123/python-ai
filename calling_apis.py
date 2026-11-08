import requests
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()

url="https://api.frankfurter.app/latest?from=USD&to=INR"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"]["INR"]
        print("Rate:", rate)
    else:
        print("Something went wrong. Status code:", response.status_code)

except Exception as e:
    print("Could not reach the API:", e)


# 2. give that data to the LLM
prompt = f'''
I have 200 NVIDIA stocks, today the price is 215$. 
How much money will I get in Indian rupees if I sell them all today.
Today's USD to INR conversion rate is {rate}
'''

# try:
#     answer = client.models.generate_content(
#         model="gemini-3.5-flash",
#         contents=prompt
#     ).text
# except Exception as e:
#     answer = f"Something went wrong: {e}"

# print(answer)

url2 = "https://api.frankfurter.app/latest?from=EUR&to=INR"

try:
    response = requests.get(url2)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"]["INR"]
        hundredEuro = rate*100
        print("100 EUR =",hundredEuro,"INR")
    else:
        print("Something went wrong. Status code:", response.status_code)
except Exception as e:
    print("Could not reach the API:", e)