import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

# Carregando o conjunto de dados California Housing
data = fetch_california_housing()

# Transformando em um DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)

# Gerando o histograma da variável ‘MedInc’
plt.hist(df["MedInc"], bins=50)
plt.xlabel("MedInc")
plt.ylabel("Frequência")
plt.show()