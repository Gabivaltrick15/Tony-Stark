import discord
import random
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

bot.run("seu codigo")
