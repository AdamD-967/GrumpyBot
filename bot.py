import os
from random import choice
from datetime import datetime as dtm
from discord.ext import commands
from memer import *
from youtube import YTDLSource

TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="wrr ")

@bot.event
async def on_ready():
    print("no elo")
    print(f"zwę się {bot.user.name}")

@bot.event
async def on_command_error(ctx, err):
    await ctx.send("No chyba nje")
    raise err


@bot.command(name="wrr")
async def wrr(ctx):
    await ctx.send("wrrr...")


@bot.command(name="nau")
async def nau(ctx):
    await ctx.send("to je "+str(dtm.now()))


@bot.command(name="dej_pan_temat")
async def show_themes(ctx):
    l = list_themes()
    message = "```\n"
    for i in l:
        message += i+'\n'
    message+="```"
    await ctx.send(message)


@bot.command(name="show_your_memes")
async def show_memes(ctx, theme: str = "manul"):
    l = list_memes(theme)
    message = "```\n"
    for i in l:
        message += i+'\n'
    message+="```"
    await ctx.send(message)


@bot.command(name="send_meme")
async def send_memes(ctx, theme: str = "manul", name: str = "manul1.jpg"):
    meme = get_meme(theme, name)
    if meme is None:
        await ctx.send("czegoś takiego to ja nie mam")
        return
    await ctx.send(file=meme)


@bot.command(name="dej_mema")
async def dej_mema(ctx, theme: str = ""):
    lt: list = list_themes()
    if theme not in lt:
        theme = choice(lt)
    meme = get_meme(theme, choice(list_memes(theme)))
    await ctx.send(file=meme)


@bot.command(name="join")
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send(f"wbiłę na {channel.name}")


@bot.command(name="leave")
async def leave(ctx):
    await ctx.voice_client.disconnect()
    await ctx.send(f"no to elo")


@bot.command(name="play")
async def play(ctx, *, url):
    async with ctx.typing():
        player = await YTDLSource.from_url(url, loop=bot.loop)
        ctx.voice_client.play(player, after=(lambda e: print(f'Player error: {e}') if e else None))

    await ctx.send(f"gram sobie {player.title}")

@bot.command(name="stop")
async def stop(ctx):
    if ctx.voice_client.is_playing():
        ctx.voice_client.stop()


@play.before_invoke
async def ensure_voice(ctx):
    if ctx.voice_client is None:
        if ctx.author.voice:
            await ctx.author.voice.channel.connect()
        else:
            await ctx.send("Się nie wziąłeś i nie połączyłeś")
    elif ctx.voice_client.is_playing():
        ctx.voice_client.stop()


bot.run(TOKEN)
