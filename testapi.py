import openai
import json

openai.api_key = "" # key in your chatgpt api key

def generate_response(prompt):
    model_engine = "text-davinci-002"
    prompt = f"{prompt}\n"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text.strip()
    return message

# example usage
prompt = "Hello, how are you?"
response = generate_response(prompt)
print(response)
