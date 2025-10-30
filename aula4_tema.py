import discord
import random
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

# Lista de emojis disponíveis
emoji_list = ["😊", "😢", "❤️", "😡", "🎉", "🍕", "😴", "😲"]

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def meme(ctx):
    bagre = random.choice(os.listdir('aula5'))
    with open(f'aula5/{bagre}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def emoji(ctx):
    escolhido = random.choice(emoji_list)
    await ctx.send(f'Aqui está um emoji para você: {escolhido}')

#OBS: esse codigo foi utilizado na aula 5, juntei mais a ídeia da aula 3, com isso fiz o tema da aula 4.

bot.run("Sua chave de bot")
