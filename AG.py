import discord
import random
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

curiosidades = [
    "Os jovens brasileiros estão se tornando uma força significativa na conscientização sobre as mudanças climáticas.",
    "Mais de 80% dos adolescentes brasileiros demonstram preocupação com o aquecimento global e as mudanças climáticas.",
    "A faixa etária mais preocupada com o aquecimento global é a Geração Z (jovens de aproximadamente 11 a 26 anos).",
    "As vacas contribuem significativamente para o aquecimento global, com efeitos negativos.",
    "O Brasil está entre os países com o maior número de animais de fazenda do mundo — incluindo bois, vacas, galinhas e frangos."
]

dicas = [
    "Deixar luzes acesas, carregar dispositivos sem necessidade ou usar aparelhos em modo stand-by consome energia, muitas vezes gerada por fontes poluentes.",
    "Banhos longos, torneiras abertas e uso desnecessário de água contribuem para o consumo de energia e escassez hídrica.",
    "Comprar roupas em excesso, especialmente de marcas que produzem em larga escala, gera muito lixo e emissão de gases poluentes.",
    "Jogar lixo reciclável no lixo comum impede que materiais sejam reaproveitados e aumenta a poluição.",
    "Optar por carros ou motos em vez de caminhar, pedalar ou usar transporte público aumenta a emissão de CO₂."
]

@bot.event
async def on_ready():
    print(f"EcoBot conectado como {bot.user}!")
    await bot.change_presence(activity=discord.Game(name="aquecimento global"))

@bot.command(name="curiosidade")
async def curiosidade(ctx):
    """Mostra uma curiosidade sobre o aquecimento global"""
    await ctx.send(random.choice(curiosidades))

@bot.command(name="dica")
async def dica(ctx):
    """Mostra uma dica ecológica"""
    await ctx.send(random.choice(dicas))

@bot.command(name="ajuda")
async def ajuda(ctx):
    """Mostra os comandos disponíveis"""
    msg = (
        "**Comandos do EcoBot**\n"
        "`!curiosidade` → mostra uma curiosidade sobre o aquecimento global\n"
        "`!dica` → dá uma dica para cuidar do planeta\n"
        "`!ajuda` → mostra esta mensagem\n"
    )
    await ctx.send(msg)

bot.run("Sua chave")
