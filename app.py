# Importando modulo do Google para converção texto para fala
import gtts

# Responsavel por tocar o som gerado
from playsound import playsound

# Abrindo arquivo criado com as frases
with open('textos.txt', 'r') as arquivo:
    for linha in arquivo:
        # Criando arquivo MP3 e reproduzindo o som
        frase = gtts.gTTS(linha, lang='pt-br')
        frase.save('texto.mp3')
        playsound('texto.mp3')