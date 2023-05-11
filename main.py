import whisper
import openai
import json
import os
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio

##whisper api
model = whisper.load_model("tiny")
result = model.transcribe("audio.mp3")
print(result["text"])


##chatgpt api
openai.api_key = ""

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
# prompt = "Hello, how are you?"
# use whisper output as prompt
prompt = result["text"]
response = generate_response(prompt)
print(response)



# (optional)create a file to save the answer of chatgpt, meaning that you could check the answer

# get the answer from chatgpt
# answer = response.choices[0].text.strip()
answer = response

# create a new txt file
with open('answer.txt', 'w') as f:
    # write answer of chatgpt to the new file
    f.write(answer)

# print if succeed
print("The answer has been saved to answer.txt file.")




# use bark to generate answer of chatgpt with voice

# download and load all models
preload_models()

# generate audio from text
""" code demo
text_prompt = """
     # Hello, my name is Suno. And, uh — and I like pizza. [laughs]
     # But I also have other interests such as playing tic tac toe.
"""
"""
text_prompt = response

audio_array = generate_audio(text_prompt)

# save audio to disk
write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)

# play text in notebook
Audio(audio_array, rate=SAMPLE_RATE)