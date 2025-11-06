import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Lista de curiosidades
curiosidades = [
    "Os jovens brasileiros estão se tornando uma força significativa na conscientização sobre as mudanças climáticas.",
    "Mais de 80% dos adolescentes brasileiros demonstram preocupação com o aquecimento global e as mudanças climáticas.",
    "A faixa etária mais preocupada com o aquecimento global é a Geração Z (jovens de aproximadamente 11 a 26 anos).",
    "As vacas contribuem significativamente para o aquecimento global, com efeitos negativos.",
    "O Brasil está entre os países com o maior número de animais de fazenda do mundo — incluindo bois, vacas, galinhas e frangos."
]

# Lista de dicas ecológicas
dicas = [
    "Deixar luzes acesas, carregar dispositivos sem necessidade ou usar aparelhos em modo stand-by consome energia, muitas vezes gerada por fontes poluentes.",
    "Banhos longos, torneiras abertas e uso desnecessário de água contribuem para o consumo de energia e escassez hídrica.",
    "Comprar roupas em excesso, especialmente de marcas que produzem em larga escala, gera muito lixo e emissão de gases poluentes.",
    "Jogar lixo reciclável no lixo comum impede que materiais sejam reaproveitados e aumenta a poluição.",
    "Optar por carros ou motos em vez de caminhar, pedalar ou usar transporte público aumenta a emissão de CO₂."
]

# Lista de perguntas do quiz
quiz_perguntas = [
    {
        "pergunta": "Qual gás é o principal responsável pelo efeito estufa?",
        "alternativas": ["Oxigênio", "Dióxido de carbono", "Nitrogênio", "Metano"],
        "resposta": 1
    },
    {
        "pergunta": "Qual dessas ações ajuda a reduzir a emissão de CO₂?",
        "alternativas": ["Usar carro todos os dias", "Reciclar lixo", "Tomar banhos longos", "Comprar roupas em excesso"],
        "resposta": 1
    },
    {
        "pergunta": "Qual fonte de energia é considerada limpa?",
        "alternativas": ["Carvão", "Petróleo", "Energia solar", "Gás natural"],
        "resposta": 2
    }
]

# Armazena perguntas pendentes por usuário
pergunta_atual = {}

@bot.event
async def on_ready():
    print(f"EcoBot conectado como {bot.user}!")
    await bot.change_presence(activity=discord.Game(name="aquecimento global"))

@bot.command(name="curiosidade")
async def curiosidade(ctx):
    await ctx.send(random.choice(curiosidades))

@bot.command(name="dica", aliases=["dicas"])
async def dica(ctx):
    await ctx.send(random.choice(dicas))

@bot.command(name="quiz")
async def quiz(ctx):
    pergunta = random.choice(quiz_perguntas)
    pergunta_atual[ctx.author.id] = pergunta
    texto = f"**{pergunta['pergunta']}**\n"
    for i, alt in enumerate(pergunta["alternativas"], start=1):
        texto += f"{i}. {alt}\n"
    texto += "\nResponda com o número da alternativa correta!"
    await ctx.send(texto)

@bot.command(name="ajuda")
async def ajuda(ctx):
    msg = (
        "**Comandos do EcoBot**\n"
        "`!curiosidade` → mostra uma curiosidade sobre o aquecimento global\n"
        "`!dica` ou `!dicas` → dá uma dica para cuidar do planeta\n"
        "`!quiz` → responde uma pergunta sobre meio ambiente\n"
        "`!ajuda` → mostra esta mensagem\n"
    )
    await ctx.send(msg)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.author.id in pergunta_atual:
        try:
            resposta = int(message.content.strip())
            pergunta = pergunta_atual[message.author.id]
            if resposta == pergunta["resposta"] + 1:
                await message.channel.send("✅ Resposta correta! Você mandou bem!")
            else:
                correta = pergunta["alternativas"][pergunta["resposta"]]
                await message.channel.send(f"❌ Resposta incorreta. A correta era: **{correta}**.")
            del pergunta_atual[message.author.id]
        except ValueError:
            await message.channel.send("Por favor, responda com o número da alternativa (1 a 4).")
        return

    await bot.process_commands(message)

# ⚠️ Substitua pelo seu token real e mantenha-o seguro
bot.run("KEY")
