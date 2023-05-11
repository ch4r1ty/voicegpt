---

---

# voicegpt

## This is a python file allowing you to talk with chatgpt, using bark, whisper and chatgptAPI

You can run this demo on macos, linux and windows.

## Configure the environment

We highly recommend you deploy the new project in a brand-new virtual environment. let's say, name of the new environment below is **voicegpt**:

```shell
conda create -n voicegpt
```

```shell
conda activate voicegpt
```

Fork and access the project file:

```shell
git clone git@github.com:ch4r1ty/voicegpt.git
```

```shell
cd voicegpt
```



## Installation

Based on whisper and bark, installing relevant packages is required. You can find more information on their pages:

### BASE

#### whisper

https://github.com/openai/whisper

#### bark

https://github.com/suno-ai/bark

#### chatgpt API

https://platform.openai.com/account/api-keys



### In short

In short, you have to run these commands for a basic usage:

#### whisper

```shell
pip install -U openai-whisper
```

```shell
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg
```

```shell
pip install setuptools-rust
```



#### bark

```shell
git clone https://github.com/suno-ai/bark
cd bark && pip install . 
```



#### Chatgpt API

You also need an openai key, which you may get for free on this website:

https://platform.openai.com/account/api-keys



## Usage

These revise of code are also required:

```python
# chatgpt api

# in "" is your openai api key

openai.api_key = ""
```

```python
# whisper api

# replace the 'tiny' with different models below

model = whisper.load_model("tiny")
result = model.transcribe("audio.mp3")
print(result["text"])
```
| Size   | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
| ------ | ---------- | ------------------ | ------------------ | ------------- | -------------- |
| tiny   | 39 M       | `tiny.en`          | `tiny`             | ~1 GB         | ~32x           |
| base   | 74 M       | `base.en`          | `base`             | ~1 GB         | ~16x           |
| small  | 244 M      | `small.en`         | `small`            | ~2 GB         | ~6x            |
| medium | 769 M      | `medium.en`        | `medium`           | ~5 GB         | ~2x            |
| large  | 1550 M     | N/A                | `large`            | ~10 GB        | 1x             |
