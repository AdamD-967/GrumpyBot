import youtube_dl as yt
import discord
import asyncio

yt.utils.bug_reports_message = lambda: ""

ytdl_opts = {
    "format": "bestaudio/best", 
    "restrictfilenames": True, 
    "outtmpl": "%(extractor)s-%(id)s-%(title)s.%(ext)s",
    "noplaylist": True, 
    "nocheckcertificate": True, 
    "ignoreerrors": False, 
    "quiet": True, 
    "no_warnings": True, 
    "default_search": "auto", 
    "source_address": "0.0.0.0"
}

ffmpeg_opts = {
    "options": "-vn"
}

ytdl = yt.YoutubeDL(ytdl_opts)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data
        self.title = data.get("title")
        self.url = data.get("url")


    @classmethod
    async def from_url(cls, url, *, loop=None, stream=True):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=(not stream)))

        if "entries" in data:
            data = data["entries"][0]

        filename = data["url"] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_opts), data=data)