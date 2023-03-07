# A.U.S.M.I. - Apenas Um Sistema Muito Inteligente
A.U.S.M.I. is a chatbot for Telegram inspired by the virtual assistant J.A.R.V.I.S., present in the Marvel universe. 

This chatbot is able to understand text and audio messages and provide responses based on a variety of topics using GPT-3.5-turbo model.

The project makes use of the following APIs:
- OpenAI's Whisper for text transcription.
- OpenAI's GPT for response generation.
- Google Text To Speech for text to speech conversion.
- Pydub for converting audio file formats.

## Demonstration
[A.U.S.M.I. Video on Youtube](http://www.youtube.com/watch?v=AHGeXzI-h68)

## Article
You can see more details about the project in the following article:

[Read A.U.S.M.I. Article on Medium](https://medium.com/@marciojmo/whisper-gpt3-5-telegram-bot-j-a-r-v-i-s-794e19da6ee3)



## Requirements
- You must have a Telegram bot created (https://telegram.me/BotFather)
- OpenAI API access token is required (https://openai.com/blog/openai-api)
- You must have python3 installed

## How to use

### 1. Cloning the repository
Clone the repository using the following command:
`git clone git@github.com:marciojmo/ausmi.git`

### 2. Installing dependencies
Navigate to your project folder and install dependencies using pip.
```
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Setting environment variables
Set the `OPENAI_TOKEN` and `TELEGRAM_TOKEN` environment variables to your respective credentials.

### 4. Running the bot
After that just run the `python3 bot.py` command.

## Live demo
Send a message /help to @ausmibot on Telegram.

The bot might not be running due to the OpenAI API limited quota.