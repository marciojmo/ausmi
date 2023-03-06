#!/usr/bin/env python
import os
import logging
import openai
import uuid
import pydub
import telegram
import gtts
from telegram.ext import filters

AUDIOS_DIR = "audios"
OPENAI_TOKEN = os.getenv("OPENAI_TOKEN")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def create_dir_if_not_exists(dir):
    if (not os.path.exists(dir)):
        os.mkdir(dir)


def generate_unique_name():
    uuid_value = uuid.uuid4()
    return f"{str(uuid_value)}"


def convert_text_to_speech(text, language_code='pt'):
    output_filepath = os.path.join(AUDIOS_DIR, f"{generate_unique_name()}.mp3")
    tts = gtts.gTTS(text=text, lang=language_code)
    tts.save(output_filepath)
    return output_filepath


def convert_speech_to_text(audio_filepath):
    with open(audio_filepath, "rb") as audio:
        transcript = openai.Audio.transcribe("whisper-1", audio)
        return transcript["text"]


async def download_voice_as_ogg(voice):
    voice_file = await voice.get_file()
    ogg_filepath = os.path.join(AUDIOS_DIR, f"{generate_unique_name()}.ogg")
    await voice_file.download_to_drive(ogg_filepath)
    return ogg_filepath


def convert_ogg_to_mp3(ogg_filepath):
    mp3_filepath = os.path.join(AUDIOS_DIR, f"{generate_unique_name()}.mp3")
    audio = pydub.AudioSegment.from_file(ogg_filepath, format="ogg")
    audio.export(mp3_filepath, format="mp3")
    return mp3_filepath


def generate_response(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": text}
        ]
    )
    answer = response["choices"][0]["message"]["content"]
    return answer


async def help_command(update: telegram.Update,
                       context: telegram.ext.ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    help_message = f"Oi {user.mention_html()}, tudo bem?\n\n"
    help_message += "Sou AUSMI, seu assistente virtual.\n"
    help_message += "Podemos conversar por texto ou por voz, você é quem manda.\n\n"
    help_message += "Use /leia [texto] se quiser que eu leia um texto para você.\n"
    help_message += "Use /ajuda para que eu repita essa mensagem! \n\n"
    help_message += "Sobre o que vamos conversar hoje? \U0001F916" # robot face emoji

    await update.message.reply_html(
        text=help_message,
        reply_markup=telegram.ForceReply(selective=True),
    )


async def read_command(update: telegram.Update,
                       context: telegram.ext.ContextTypes.DEFAULT_TYPE) -> None:
    text = " ".join(context.args)
    if len(text) <= 0:
        no_text_message = "Informe o texto após o comando! \U0001F620"
        return await update.message.reply_text(text=no_text_message)
    audio_path = convert_text_to_speech(text)
    await update.message.reply_audio(audio=audio_path)


async def handle_text(update: telegram.Update,
                      context: telegram.ext.ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    answer = generate_response(text)
    await update.message.reply_text(answer)


async def handle_voice(update: telegram.Update,
                       context: telegram.ext.ContextTypes.DEFAULT_TYPE) -> None:
    ogg_filepath = await download_voice_as_ogg(update.message.voice)
    mp3_filepath = convert_ogg_to_mp3(ogg_filepath)
    transcripted_text = convert_speech_to_text(mp3_filepath)
    answer = generate_response(transcripted_text)
    answer_audio_path = convert_text_to_speech(answer)
    await update.message.reply_audio(audio=answer_audio_path)
    os.remove(ogg_filepath)
    os.remove(mp3_filepath)
    os.remove(answer_audio_path)


def main() -> None:
    create_dir_if_not_exists(AUDIOS_DIR)

    openai.api_key = OPENAI_TOKEN

    application = telegram.ext.Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(telegram.ext.CommandHandler("leia", read_command))
    application.add_handler(telegram.ext.CommandHandler("ajuda", help_command))
    application.add_handler(telegram.ext.MessageHandler(
        filters.TEXT & ~filters.COMMAND, handle_text))
    application.add_handler(telegram.ext.MessageHandler(
        filters.VOICE, handle_voice))

    application.run_polling()


if __name__ == "__main__":
    main()
