from datetime import datetime
import requests
import time
import os

# 1. URL configurada para trazer Dólar, Euro e Bitcoin de uma vez só
url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

print("Iniciando a coleta Multimoedas (CSV)... Pressione CTRL+C para parar.\n")

# Verificação inicial: se o arquivo CSV não existir, criamos o cabeçalho (as colunas da planilha)
arquivo_csv = "historico_moedas.csv"
if not os.path.exists(arquivo_csv):
    with open(arquivo_csv, "a") as arquivo:
        arquivo.write("data_hora,moeda,preco\n")

while True:
    try:
        requisicao = requests.get(url)
        dados = requisicao.json()

        agora = datetime.now()
        data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")

        # 2. Como a API traz as 3 moedas, isolamos o 'bid' (preço) de cada uma delas
        preco_dolar = float(dados['USDBRL']['bid'])
        preco_euro = float(dados['EURBRL']['bid'])
        preco_bitcoin = float(dados['BTCBRL']['bid'])

        # Mostramos o painel atualizado no terminal
        print(f"[{data_formatada}] Leituras Realizadas:")
        print(f"   💵 Dólar: R$ {preco_dolar}")
        print(f"   💶 Euro:  R$ {preco_euro}")
        print(f"   🪙 BTC:   R$ {preco_bitcoin}")

        # 3. Abrimos o arquivo .csv e salvamos cada uma em uma linha nova (Formato Planilha)
        with open(arquivo_csv, "a") as arquivo:
            arquivo.write(f"{data_formatada},USD,{preco_dolar}\n")
            arquivo.write(f"{data_formatada},EUR,{preco_euro}\n")
            arquivo.write(f"{data_formatada},BTC,{preco_bitcoin}\n")
            
    except requests.exceptions.RequestException as erro:
        agora = datetime.now()
        data_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")
        print(f"[{data_formatada}] ⚠️ Erro de rede ao coletar dados. Tentando novamente...")
        
    print("-" * 40)
    time.sleep(5)