import json
import calendar
from datetime import date
from operator import index
import pandas as pd
import numpy as np
import csv
import streamlit as st
from datetime import datetime 

ano = date.today().year
mes = date.today().month
dia = date.today().day
dataHoje = str(date.today())
# data = calendar.TextCalendar(calendar.SUNDAY)

dia_semana = calendar.weekday(ano, mes, dia) #atualizar na sexta / dia da semana retorna seg==0,ter==1,qua==2,qui==3,sex==4, sab==5,DO==6

nomes = np.loadtxt(fname = "nomes.txt", dtype=str)
print(nomes, dataHoje)
# se for sexta e a data da ultima atualizaçã 'nome[0] for diferente de hoje'
if dia_semana == 2 and nomes[0] != dataHoje: ## nome[0] quarda a data da ultima atualização //data precisa ser diferente para atualizar uma vez no dia escolhido -> 'Sexta' // apos isso a data passa á ser igual impedindo atualizar ate a proxima sexta.
    nomes[0] = dataHoje
    n = nomes[6]
    nomes = np.delete(nomes,(6),axis=0)
    nomes = np.insert(nomes, 1, n)
    nomes = nomes.tolist()
    arquivo = open('nomes.txt', 'w')
    for x in range(7):
        lista=nomes[x]
        arquivo.write(lista+"\n")
    
    with open('listapaes.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        # spamwriter.writerow(['Lista de Quem Traz Paes'])
        spamwriter.writerow(['Segunda','Terca','Quarta','Quinta','Sexta'])
        spamwriter.writerow(nomes[1:6])
    
    df = pd.read_csv('listapaes.csv', sep = ';')
    df.style.format({'VENDAS':'R$ {:,.0f}'}).bar(color='Green')
        
    checkbox_mostrar_tabela = st.sidebar.checkbox('Mostrar tabela')
    if checkbox_mostrar_tabela:
        df = pd.read_csv('listapaes.csv', sep = ';')   

        st.sidebar.markdown('## Filtro para a tabela')
        categorias = list(df)
        categoria = st.sidebar.selectbox('Selecione a categoria para apresentar na tabela', options = categorias)
        
        st.title('aaaaaaaaa')
        if categoria == 'Segunda':
            df['Segunda']
        elif categoria == 'Terca':
            df['Terca']
        elif categoria == 'Quarta':
            df['Quarta']
        elif categoria == 'Quinta':
            df['Quinta']
        else:
            df['sexta']
    else:
        st.title('bbbbbbb')
        df = pd.read_csv('listapaes.csv', sep = ';')       
        st.sidebar.markdown('## Filtro para a tabela')
        st.write(df.head())

else: 
    checkbox_mostrar_tabela = st.sidebar.checkbox('Mostrar tabela')
    if checkbox_mostrar_tabela:

        df = pd.read_csv('listapaes.csv', sep = ';')       
        st.sidebar.markdown('## Filtro para a tabela')
        categorias = list(df)
        categoria = st.sidebar.selectbox('Selecione a categoria para apresentar na tabela', options = categorias)
        st.sidebar.markdown('## Filtro para o gráfico')

        st.title('aaaaaaaaa')
        if categoria == 'Segunda':
            df['Segunda']
        elif categoria == 'Terca':
            df['Terca']
        elif categoria == 'Quarta':
            df['Quarta']
        elif categoria == 'Quinta':
            df['Quinta']
        else:
            df['Sexta']
    else:
        st.title('bbbbbbb')
        df = pd.read_csv('listapaes.csv', sep = ';')       
        st.sidebar.markdown('## Filtro para a tabela')
        st.write(df.head())



