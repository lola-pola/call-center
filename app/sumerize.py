import openai
import os

openai.api_type = "azure"
openai.api_base = os.getenv("URL_AZURE_AI_DEVINCHI")
openai.api_version = "2022-12-01"
openai.api_key = os.getenv("KEY_AZURE_AI_DEVINCHI")




def find_keywords(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Extract keywords from: " + text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        best_of=1,
        stop=None

    )

    keywords = response.choices[0].text
    return keywords.strip().split("\n")

