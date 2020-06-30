#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[3]:


import pandas as pd
import numpy as np


# In[4]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[5]:


black_friday


# In[6]:


black_friday.head()


# In[7]:


black_friday.shape


# In[8]:


black_friday.info()


# In[8]:





# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[9]:


def q1():
    return black_friday.shape


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[10]:


def q2():
    # Melhor solucao
    # black_friday.query("Gender == 'F' & Age == '26-35'").shape[0]

    # Retorne aqui o resultado da questão 2.
    # Minha solucao
    black_friday_idade_26_35 = black_friday[black_friday['Age']=='26-35']
    black_friday_idade_26_35_F = black_friday_idade_26_35[black_friday_idade_26_35['Gender']=='F']
    return  black_friday_idade_26_35_F.shape[0]


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[11]:


def q3():
    # Melhor solucao
    # len(black_friday['User_ID'].unique())

    # Retorne aqui o resultado da questão 3.
    black_friday_usuarios = black_friday['User_ID'].value_counts()
    return black_friday_usuarios.shape[0]

q3()


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[12]:


def q4():
    # Retorne aqui o resultado da questão 4.
    # melhor solucao
    # (len(tipos_de_dados.dtypes.unique()))
    #####################
    #Minha solucao
    array_tipos_dados = []
    tipos_de_dados = pd.DataFrame(black_friday)

    for i in tipos_de_dados.dtypes.value_counts():
      array_tipos_dados.append(i)


    return len(array_tipos_dados)

q4()


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[57]:


def q5():
    # Melhor solucao:
    # https://github.com/BrunoDorneles/aceleradev-datascience/blob/master/Semana%202/Manipula%C3%A7%C3%A3o%20de%20Dados.ipynb
    # black_friday.isnull().sum().max() / black_friday.shape[0]
    # Retorne aqui o resultado da questão 5.
    quantidade_total_registro = black_friday.shape[0]
    quantidade_total_valores_nulos_por_colunas = (black_friday.isnull().sum())
    quantidade_total_valores_nulos = quantidade_total_valores_nulos_por_colunas.max()
    return float(quantidade_total_valores_nulos / quantidade_total_registro)
    #print(x)
    #print(pd.DataFrame(black_friday.isna().sum() / (black_friday.shape[0])))

q5()


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[60]:


def q6():
    # melhor solucao:
    # black_friday.isna().sum().max()
    # Retorne aqui o resultado da questão 6.
    valores_nulos_df = black_friday.isna().sum()
    return  int(valores_nulos_df.max())

q6()


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[15]:


def q7():
    # Retorne aqui o resultado da questão 7.
    pass


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[16]:


def q8():
    # Retorne aqui o resultado da questão 8.
    pass


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[17]:


def q9():
    # Retorne aqui o resultado da questão 9.
    pass


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[18]:


def q10():
    # Retorne aqui o resultado da questão 10.
    pass

