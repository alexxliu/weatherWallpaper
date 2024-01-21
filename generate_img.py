import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def generateImg(prompt):
    response = client.images.generate(
        prompt = prompt,
        model="dall-e-3",
        n = 1,
        size = "1792x1024"
    )

    img_url = response.data[0].url

    return img_url