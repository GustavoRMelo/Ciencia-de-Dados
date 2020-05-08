# 1- Questão ou definição do problema.
# 2- Obtenha dados de treinamento e dados de teste.
# 3- Discuta, prepare e limpe os dados.
# 4- Analise, identifique padrões e explore os dados.
# 5- Modele, faça previsão e solucione o problema.
# 6- Visualize, relate e apresente os passos da solução do problema e a solução final.
# 7- Submeta os resultados.
import pandas as pd

train_df = pd.read_csv('C:/Users/Gustavo/OneDrive/Documents/Became a Python Developer/Introduction/train.csv')
test_df = pd.read_csv('C:/Users/Gustavo/OneDrive/Documents/Became a Python Developer/Introduction/test.csv')
combine = [train_df, test_df]

#Descrição

print(train_df.columns.values)

train_df.head()
