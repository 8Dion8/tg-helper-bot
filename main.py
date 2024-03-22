import telebot as tb
from telebot.types import InputFile
from dotenv import dotenv_values
import re

import func.core as bot_core_lib
import func.youtube as bot_func_youtube

config = dotenv_values(".env")
TOKEN = config["TOKEN"]
AUTHOR_TG_ID = config["AUTHOR_TG_ID"]

YOUTUBE_LINK_REGEX = r"(.*(www\.youtube\.com\/.+|youtu\.be\/.+)|(.+))"



bot = tb.TeleBot(TOKEN, parse_mode="MARKDOWN")


bot.send_message(AUTHOR_TG_ID, "Bot online.")


@bot.message_handler(func=lambda message: True)
def general_handler(message):
    text = message.text
    chat_id = message.chat.id

    if re.match(YOUTUBE_LINK_REGEX, text):
        youtube_handler(message)



@bot.message_handler(commands=["y", "youtube"])
def youtube_handler(message):
    text = message.text
    chat_id = message.chat.id
    

    content_regex = re.match(YOUTUBE_LINK_REGEX, text)
    if content_regex:
        bot_core_lib.handle_user_dir_creation(str(chat_id))
        yt_link_group = content_regex.group(2)
        if yt_link_group:
            yt_link = content_regex.group(2)
            #bot.send_message(chat_id, f"found yt link: `{yt_link}`")
            video_info = bot_func_youtube.get_video_info(yt_link)
            video_info_formatted = "\n".join(f"{key}: {val}" for key, val in video_info.items())
            bot.send_message(chat_id, video_info_formatted)
            download_path = f"usrstorage/{chat_id}/" 
            downloaded_file_path = bot_func_youtube.download_from_yt(yt_link, download_path)
            
            bot.send_video(chat_id, InputFile(downloaded_file_path))
            return 0
        yt_search_query = content_regex.group(3)
        if yt_search_query:
            bot.send_message(chat_id, f"found search query: `{yt_search_query}`")
            return 0
    else:
        bot.send_message(chat_id, "there is nothing we can do...")







bot.infinity_polling()
