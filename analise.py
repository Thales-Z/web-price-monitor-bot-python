import pandas as pd
import matplotlib.pyplot as plt

# 1. O Pandas processa tudo
df = pd.read_csv("historico_moedas.csv")
relatorio = df.groupby('moeda')['preco'].agg(['min', 'max']).reset_index()
relatorio['variacao_%'] = ((relatorio['max'] - relatorio['min']) / relatorio['min']) * 100

print("--- RELATÓRIO DE OSCILAÇÃO DO MERCADO ---")
print(relatorio.to_string(index=False))

# 2. O Pandas desenha o gráfico limpo e moderno (Sem usar o navegador)
relatorio.plot(x='moeda', y='variacao_%', kind='bar', color='#4F46E5', legend=False)

# Customização minimalista
plt.title('Volatilidade das Moedas (%)', fontsize=12, fontweight='bold', pad=15)
plt.ylabel('Variação %')
plt.xlabel('') 
plt.xticks(rotation=0) # Nomes das moedas na horizontal

plt.tight_layout()
plt.show() # Abre a janela direto na tela, 100% seguro contra erros de rede