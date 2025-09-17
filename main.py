from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv(override=True)

openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key:
    print(f"OpenAI API Key exists")
else:
    print("OpenAI API Key not set")

def callOpenAILLM():
    openai = OpenAI()
    messages = [{"role": "user", "content": "What is 100*456?"}]
    response = openai.chat.completions.create(
        model="gpt-4.1-nano",
        messages=messages
    )
    print(response.choices[0].message.content)

    question = "Please propose a hard, challenging question to assess someone's IQ. Respond only with the question."
    messages = [{"role": "user", "content": question}]
    response = openai.chat.completions.create(
     model="gpt-4.1-mini",
     messages=messages
    )

    question = response.choices[0].message.content

    print(question)

if __name__ == "__main__":
    callOpenAILLM()
    


