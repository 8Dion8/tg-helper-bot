import telebot as tb
from dotenv import dotenv_values
import re

import func.youtube as bot_func_youtube

config = dotenv_values(".env")
TOKEN = config["TOKEN"]
AUTHOR_TG_ID = config["AUTHOR_TG_ID"]



bot = tb.TeleBot(TOKEN, parse_mode="MARKDOWN")

bot.send_message(AUTHOR_TG_ID, "Bot online.")

@bot.message_handler(commands=["y", "youtube"])
def youtube_handler(message):
    text = message.text
    chat_id = message.chat.id

    content_regex = re.search(r"(\/youtube|\/y)\s(.*(www\.youtube\.com\/.+|youtu\.be\/.+)|(.+))", text)

    if content_regex:
        yt_link = content_regex.group(3)
        if yt_link:
            bot.send_message(chat_id, f"found yt link: `{yt_link}`")
            return 0
        yt_search_query = content_regex.group(4)
        if yt_search_query:
            bot.send_message(chat_id, f"found search query: `{yt_search_query}`")
            return 0
    else:
        bot.send_message(chat_id, "there is nothing we can do...")



    bot.send_message(chat_id, text)


bot.infinity_polling()
