from googletrans import Translator

mensagem = "axmabgdlhvvtlbhglpaxgtkhuhmabmltghulmtvextgwkxjnbkxlaxeiykhftitllxkurtkxtvknvbteitkmhymaxanftgkhuhmkxetmbhglabimxvaghehzrvtguxtwhktuexbybmgxxwlhnktllblmtgvxpxebdxtkhuhmmatmgxxwlnltubmtgwpaxgpxaxeimaxkhuhmbmvkxtmxltuhgwVnkbhnlerflVtlxblvkbmbvtehymaxlmtklabimxvaghehzbxlwxeboxkrkhuhmlmatmixiixkmaxitoxfxgmlhyfbemhgdxrgxl"

# Calcula todas as possibilidades:
for deslocamento in range(26):
    # Declara o espaço da mensagem decodificada
    mensagem_decodificada = ""
    # Para cada letra em mensagem, faça:
    for letra in mensagem:
        # Caso a letra seja do alfabeto:
        if letra.isalpha():
            # Compute uma nova letra, onde você considera (o valor equivalente da letra na tabela ascii, o deslocamento e o limite da tabela ascii), recolha o resto da divisão por 26 e acrescente 97.
            nova_letra = chr((ord(letra) - deslocamento - 97) % 26 + 97)
        # Caso não seja do alfabeto:
        else:
            # Repita o caractere da entrada.
            nova_letra = letra
        # Concatene todas as novas letras em uma só mensagem:
        mensagem_decodificada += nova_letra
    # Imprima todas as 26 possibilidades e compare com a mensagem original
    # print(f"Deslocamento {deslocamento}: {mensagem_decodificada}\n"
          # f"Mensagem: {mensagem}\n")
# Como eu sei qual é a correta?
# Será aquela mensagem decodificada que apresenta um texto legível.
# Aqui no caso é o deslocamento 19 como legível na língua inglesa.
# hethinksoccasionswhenarobothitsanobstacleandrequireshelpfromapasserbyareacrucialpartofthehumanrobotrelationshiptechnologycanbeadorableifitneedsourassistancewelikearobotthatneedsusabitandwhenwehelptherobotitcreatesabondwuriouslymswaseiscriticalofthestarshiptechnologiesdeliveryrobotsthatpepperthepavementsofmiltonkeynes
# he thinks occasions when a robot hits an obstacle and requires help from a passer by area crucial part of the human robot relationship technology can be adorable if it needs our assistance we like a robot that needs usabit and when we help the robot it creates a bond wuriouslyms wase is critical of the starship technologies delivery robots that pepper the pavements of milton keynes

# Traduzindo para o portugues:

# Criar um objeto Translator
translator = Translator()

# Define a string a ser traduzida
texto = "he thinks occasions when a robot hits an obstacle and requires help from a passer by area crucial part of the human robot relationship technology can be adorable if it needs our assistance we like a robot that needs usabit and when we help the robot it creates a bond wuriouslymswase is critical of the starship technologies delivery robots that pepper the pavements of milton keynes"

# Realiza a tradução
traducao = translator.translate(texto, src='en', dest='pt')

# Imprime a tradução
print(traducao.text)

