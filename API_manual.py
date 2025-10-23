import random
sulista = 0
def get_emoji(sentimento):
    emojis = {
        "feliz": "😄",
        "triste": "😢",
        "amor": "❤️",
        "raiva": "😡",
        "surpreso": "😲",
        "medo": "😱",
        "sono": "😴",
        "risada": "😂"
    }

    sentimento = sentimento.lower()
    return emojis.get(sentimento, "🤔")  # 🤔 

print(get_emoji("feliz"))     # 😄
print(get_emoji("triste"))    # 😢
