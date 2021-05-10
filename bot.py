import os
from datetime import datetime as dtm
from dotenv import load_dotenv
import discord
from discord.ext import commands
from memer import *

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="wrr ")

@bot.event
async def on_ready():
    print("no elo")
    print(f"zwę się {bot.user.name}")

@bot.event
async def on_command_error(ctx, err):
    await ctx.send("No chyba nje")


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


bot.run(TOKEN)
