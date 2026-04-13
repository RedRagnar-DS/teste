import pandas as pd
import matplotlib.pyplot as plt

dados = {
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Curitiba', 'Salvador', 'Manaus'],
    'Temperatura': [46.5, 34.2, 22.0, 31.8, 33.5],
    'Umidade': [60, 75, 55, 80, 90],
    'Velocidade do vento': ['20kmh', '50kmh', '15kmh', '16kmh', '20kmh']
}

df = pd.DataFrame(dados)

print("Dados carregados com sucesso!")
print(df)

#Calculando métircas importantes
temp_media = df['Temperatura'].mean()
cidade_quente = df.loc[df['Temperatura'].idxmax(), 'Cidade']
cidade_fria = df.loc[df['Temperatura'].idxmin(), 'Cidade']

print("\n"f"A temperatura média geral é: {temp_media:.2f}ºC")
print(f"A cidade mais quente é: {cidade_quente}")
print(f"A cidade mais fria é: {cidade_fria}")

#Criando o gráfico
plt.figure(figsize=(10,6))
plt.bar(df['Cidade'], df['Temperatura'], color=['skyblue', 'orange', 'lightgreen', 'red', 'darkred'])

#customização
plt.title('Comparativo de temperatura por Cidades', fontsize=14)
plt.xlabel('Cidade')
plt.ylabel('Temperatura (°C)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

#Exibindo
plt.show()