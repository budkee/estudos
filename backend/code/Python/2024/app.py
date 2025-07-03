import logging
import datetime
import atexit
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

# ------------------ Configurações da Applicação ------------------
app = Flask(__name__)
# Configurar o logging básico
logging.basicConfig(level=logging.INFO)

last_run_time = None

# Visão do Browser
@app.route('/')
def cron_status():
    global last_run_time
    return f"Última vez que o job foi executado: {last_run_time}"

def job():
    """
        --> O que será realizado neste job?
        1. Envio de e-mails periódicos.
        
        --> Pré-requisitos:
        - Boletim formatado

        # -------- Roadmap do Endpoint | newsletter/send-email --------
        1. Recuperar os usuários inscritos e seus períodos de preferência
                -> Via nws_service.UserService.get_user_by_email()
            2. Recuperar os dados das condições climáticas
                -> Via nws_service.NewsletterService.get_weather_data_from_api()
                -> Via weather_service.WeatherService.parse_weather_data()
            3. Formatar o boletim
                -> Via nws_service.NewsletterService.formatar_newsletter()
        4. Enviar o e-mail(boletim) conforme a sequência escolhida

        # -------- Entradas | Weather --------
        2. Recuperar os dados das condições climáticas
            Endpoint ['POST']: http://127.0.0.1:5002/weather/collect

        3. Formatar o boletim no serviço de dados: ao realizar a coleta de uma localidade, é ativado o gatilho para que essa função seja executada e a formatação do boletim fique pronta para coleta via
            --> Separar por frequência['minute','weekly', 'biweekly', 'monthly', 'semiannual']
                -> Via nws_service.UserService.get_user_by_email()
                --> Formatar o boletim de acordo com a frequência
                    -> Via 
                retornar listas de dados separadas por frequência. Ex.: formatted_weather_forecast(minute_forecast, weekly_forecast, biweekly_forecast, monthly_forecast, semiannual_forecast.
        
        # -------- Saídas | Newsletter --------
        1. Recuperar os usuários inscritos e seus períodos de preferência
            -> Via nws_service.UserService.get_user_by_email()

    """
    # ---------- Log do tempo de execução ----------
    global last_run_time
    last_run_time = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    app.logger.info(f"Job foi executado às: {last_run_time}")

    # ---------- Enviar e-mails aos usuários inscritos no serviço ----------

# Inicializar um objeto do scheduler
agendamento = BackgroundScheduler()
agendamento.start()


# Agendar o trabalho(job) para ser feito a cada minuto. | Visão do Console
agendamento.add_job(
    func=job,
    trigger=IntervalTrigger(minutes=1),
    id='my_cron_job_id',
    name='Trabalho: Impressão no console.',
    replace_existing=True
)

# Parar com o agendamento ao encerrar a aplicação
atexit.register(lambda: agendamento.shutdown())

# ------------------ Início da Applicação ------------------
if __name__ == '__main__':
    app.run(debug=True)