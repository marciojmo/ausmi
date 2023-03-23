# A.U.S.M.I. - Apenas Um Sistema Muito Inteligente

Welcome to the A.U.S.M.I. chatbot for Telegram, inspired by the virtual assistant J.A.R.V.I.S. from the Marvel universe. 

A.U.S.M.I. uses the GPT-3.5-turbo model to generate responses based on various topics, and is able to understand both text and audio messages.

To make this possible, the project utilizes several APIs including OpenAI's Whisper for text transcription, OpenAI's GPT for response generation, Google Text To Speech for text to speech conversion, and Pydub for audio file format conversion.

To learn more about the project, please see the A.U.S.M.I. article on Medium, which provides detailed information:
[A.U.S.M.I. Article on Better Programming](https://medium.com/@marciojmo/whisper-gpt3-5-telegram-bot-j-a-r-v-i-s-794e19da6ee3)

You may also want to check A.U.S.M.I. demo on Youtube:
[A.U.S.M.I. Demo on Youtube](http://www.youtube.com/watch?v=AHGeXzI-h68)

## Requirements
To use A.U.S.M.I., you will need a Telegram bot, OpenAI API access token, and python3 installed. Ensure that the `OPENAI_TOKEN` and `TELEGRAM_TOKEN` environment variables are set with your respective credentials.

You may also need to install ffmpeg (ubuntu example)
```
sudo apt-get -y update
sudo apt-get install -y ffmpeg
```

## Getting started
Follow the steps below to get started:

Clone the repository using the command: 
```
git clone git@github.com:marciojmo/ausmi.git
```

Navigate to your project folder and install dependencies using pip:
```
pip install --upgrade pip
pip install -r requirements.txt
```

 Run the command to start the bot.
```
python3 bot.py
```

Alternatively, if you have Docker installed, you can run A.U.S.M.I. inside a Docker container by following these instructions:

Build the bot image using the Dockerfile located in the project root folder with this command: 
```
docker build -t ausmi .
```

Run the bot container ensuring you specify your OpenAI and Telegram tokens: 
```
docker run -d -e OPENAI_TOKEN=<your_openai_token> -e TELEGRAM_TOKEN=<your_telegram_token> ausmi
```

## Schrodinger`s Live Demo
You can see a live demo of A.U.S.M.I. by sending `/ajuda` to `@ausmibot` on Telegram. Note that the bot might or might not be running due to its limited budget for accessing OpenAI`s APIs.