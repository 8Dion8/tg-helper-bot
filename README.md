# Helper Telegram Bot

## Usage
### Commands
* /y /youtube <link> - Download video from YouTube from link
* /y /youtube <query> - Download video from Youtube by searching (WIP)
* /i /image - Image operations (resize, change type, recolor?)
* /s /sticker - Automatically convert image/video to format needed for stickers
* /v /video - Video operations (extract audio, ?)
* /t /songtag - Automatically format an mp3 with album cover, artist, etc

## Development
Needs a `.env` in the root directory with the following content to start the bot:
```
TOKEN=<telegram bot token>
AUTHOR_TG_ID=<telegram id of developer for debug messages>
```
