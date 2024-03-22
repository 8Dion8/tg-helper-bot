import yt_dlp
import json

def get_video_info(link: str) -> dict:
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




def download_from_yt(link: str, download_path: str) -> str:
    link_hash = hash(link)
    download_path = f"{download_path}{link_hash * -1 if link_hash < 0 else link_hash}.mp4"
    opts = {
        'outtmpl': download_path,
        'format': 'best/best',
    }
    with yt_dlp.YoutubeDL(opts) as ytdl:
        video_info = ytdl.extract_info(link, download=False)

        ytdl.download(link)

    return download_path



