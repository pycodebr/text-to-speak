import pyttsx3

# Carrega a lib #
engine = pyttsx3.init()

# Texto que a engine vai falar #
engine.say('Olá, como você está?')
engine.say('Em qual linguagem você programa?')

# Executa #
engine.runAndWait()