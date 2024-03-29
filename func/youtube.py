import yt_dlp
import json
import re


class YTHandler:

    def __init__(self, bot):
        self.bot = bot

    def get_video_info(self, link: str) -> dict:
        opts = {}
        with yt_dlp.YoutubeDL(opts) as ytdl:
            video_info = ytdl.extract_info(link, download=False)
            raw_info = ytdl.sanitize_info(video_info)
            filtered_info = {
                "Title": raw_info["title"],
                "Channel": raw_info["channel"],
                "Duration": f"{raw_info['duration']//60}min {raw_info['duration']%60}s",
            }
            return filtered_info




    def download_from_yt(self, link: str, download_path: str, tdcid: int, tdmid: int) -> str:

        def progress_hook(d):
            if d['status'] == 'downloading':
                progress = re.findall(r"\d+\.\d+%", d['_percent_str'])[0]
                self.bot.edit_message_text(chat_id=tdcid, message_id=tdmid, text=f"Downloading:{progress}")


        link_hash = hash(link)
        download_path = f"{download_path}{link_hash * -1 if link_hash < 0 else link_hash}.mp4"
        opts = {
            'outtmpl': download_path,
            'format': 'best/best',
            'progress_hooks': [progress_hook]
        }
        with yt_dlp.YoutubeDL(opts) as ytdl:
            video_info = ytdl.extract_info(link, download=False)

            ytdl.download(link)

        return download_path



