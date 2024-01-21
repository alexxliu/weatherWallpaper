import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generatePrompt(weatherInfo):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are generating a description used for wallpaper art generation"},
        {"role": "user", "content": "In less than 800 characters, given the following weather information, create directions for a digital/anime art style wallpaper that matches the vibe of the given weaether conditions:"},
        {"role": "user", "content": weatherInfo}

    ]
    )

    return response.choices[0].message.content
