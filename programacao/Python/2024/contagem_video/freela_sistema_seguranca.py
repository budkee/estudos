import cv2
import numpy as np
import subprocess

# Carregar os arquivos do YOLO
modelo_cfg = './yolo/yolov3.cfg'
modelo_pesos = './yolo/yolov3.weights'
coco_nomes = './yolo/coco.names'

# Carregar nomes das classes
with open(coco_nomes, 'r') as f:
    classes = [linha.strip() for linha in f.readlines()]

# Carregar a rede YOLO
rede = cv2.dnn.readNet(modelo_pesos, modelo_cfg)
nomes_camadas = rede.getLayerNames()
camadas_saida = [nomes_camadas[i - 1] for i in rede.getUnconnectedOutLayers()]

# Função para contar objetos
def contar_objetos(caminho_video):
    # Inicializar contadores
    qtd_carro = 0
    qtd_moto = 0
    qtd_pessoa = 0
    qtd_bicicleta = 0
    qtd_onibus = 0
    qtd_caminhao = 0

    # Carregar vídeo
    captura = cv2.VideoCapture(caminho_video)
    
    while captura.isOpened():
        ret, quadro = captura.read()
        if not ret:
            break

        # Pré-processar o quadro para YOLO
        altura, largura, canais = quadro.shape
        blob = cv2.dnn.blobFromImage(quadro, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        rede.setInput(blob)
        saidas = rede.forward(camadas_saida)

        # Analisar saídas
        ids_classes = []
        confiancas = []
        caixas = []
        for saida in saidas:
            for detecao in saida:
                scores = detecao[5:]
                id_classe = np.argmax(scores)
                confianca = scores[id_classe]
                if confianca > 0.5:
                    # Obter coordenadas da caixa delimitadora
                    centro_x = int(detecao[0] * largura)
                    centro_y = int(detecao[1] * altura)
                    w = int(detecao[2] * largura)
                    h = int(detecao[3] * altura)
                    x = int(centro_x - w / 2)
                    y = int(centro_y - h / 2)
                    caixas.append([x, y, w, h])
                    confiancas.append(float(confianca))
                    ids_classes.append(id_classe)

        # Aplicar Non-Max Suppression (NMS) para eliminar caixas sobrepostas
        if len(caixas) > 0:
            indices = cv2.dnn.NMSBoxes(caixas, confiancas, 0.5, 0.4)

            # Verificação para garantir que os índices estejam dentro do intervalo
            if len(indices) > 0:
                for i in indices.flatten():
                    if i < len(ids_classes) and i < len(caixas):  # Verifica se o índice está dentro do intervalo
                        rotulo = str(classes[ids_classes[i]])
                        if rotulo == 'car':
                            qtd_carro += 1
                        elif rotulo == 'motorbike':
                            qtd_moto += 1
                        elif rotulo == 'person':
                            qtd_pessoa += 1
                        elif rotulo == 'bicycle':
                            qtd_bicicleta += 1
                        elif rotulo == 'bus':
                            qtd_onibus += 1
                        elif rotulo == 'truck':
                            qtd_caminhao += 1

                        # Mostrar o frame com os objetos detectados (opcional)
                        if i < len(caixas):
                            x, y, w, h = caixas[i]
                            confianca = confiancas[i]
                            cor = (0, 255, 0)
                            cv2.rectangle(quadro, (x, y), (x + w, y + h), cor, 2)
                            cv2.putText(quadro, f'{rotulo} {confianca:.2f}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, cor, 2)

        cv2.imshow("Vídeo", quadro)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    captura.release()
    cv2.destroyAllWindows()

    # Mostrar contagens finais
    print(f"Carros: {qtd_carro}")
    print(f"Motos: {qtd_moto}")
    print(f"Pedestres: {qtd_pessoa}")
    print(f"Bicicletas: {qtd_bicicleta}")
    print(f"Ônibus: {qtd_onibus}")
    print(f"Caminhões: {qtd_caminhao}")

# Função para converter vídeos MOV para MP4
def converter_mov_para_mp4_ffmpeg(caminho_entrada, caminho_saida):
    comando = ['ffmpeg', '-i', caminho_entrada, '-vcodec', 'h264', '-acodec', 'mp2', caminho_saida]
    subprocess.run(comando)

# Exemplo de uso
# caminho_entrada = './videos/900_910.mov'
caminho_entrada = './videos/700_710.mov'
caminho_saida = './videos/mp4/700_710.mp4'
# converter_mov_para_mp4_ffmpeg(caminho_entrada, caminho_saida)
contar_objetos(caminho_saida)
