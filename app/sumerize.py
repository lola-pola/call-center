import openai
import os

# Set up API key
openai.api_key = os.environ['KEY_AZURE_AI']

def find_keywords(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Extract keywords from: " + text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    keywords = response.choices[0].text
    return keywords.strip().split("\n")

