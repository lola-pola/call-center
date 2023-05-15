import openai
import os

openai.api_type = "azure"
openai.api_base = "https://aks-production.openai.azure.com/" 
openai.api_version = "2022-12-01"
openai.api_key = os.getenv("KEY_AZURE_AI_DEVINCHI")


def find_keywords(text):
    response = openai.Completion.create(
        engine="call-center",
        prompt="Extract keywords from: " + text,
        max_tokens=1024,
        n=1,
        temperature=0.5,
        stop=None

    )

    keywords = response.choices[0].text
    return keywords.strip().split("\n")

