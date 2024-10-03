import os
from twilio.rest import Client

# Substitua pelos valores da sua conta Twilio
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

# Enviando a mensagem
message = client.messages.create(
    from_='whatsapp:+14155238886',  # Número de WhatsApp do Twilio Sandbox
    body='Olá! Esta é uma mensagem de teste do Twilio.',
    to='whatsapp:+5567992626362'  # Substitua pelo seu número de WhatsApp com o código do país
)

print(f"Mensagem enviada com SID: {message.sid}")
