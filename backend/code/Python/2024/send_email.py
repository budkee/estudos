import smtplib
import email.message

def enviar_email():
    corpo = """
    <h2>O que foi feito? </h2>
    <p> Atividade A</p>
    <p> Atividade B</p>

    <h2>Problemas? </h2>
    <p> Problema A</p>
    <p> Problema B</p>
    """

    # Organizando o email
    msg = email.message.Message()
    msg['Subject'] = "Relatório da Semana | Site"
    msg['From'] = "kae.budke@gmail.com"
    msg['To'] = "kae.budke@gmail.com"
    pwd = 'pxmzaxqhclapugpq'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo)

    # Comunicação com o servidor
    servidor = smtplib.SMTP('smtp.gmail.com: 587')
    servidor.starttls()
    servidor.login(msg['From'], pwd)
    servidor.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
    print('Email enviado com sucesso!')

if __name__ == '__main__':
    
    enviar_email()