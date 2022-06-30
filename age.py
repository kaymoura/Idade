import datetime #Modulo da biblioteca
from datetime import date #Classe date 

# Repete o simbolo 
print('='*27)
print('     CALCULO DE IDADE')
print('='*27)
print('\n Informe os seguintes dados:')

# Entrada de dados
dia = int(input('\n Que dia voce nasceu? '))
mes = int(input(' Qual mes voce nasceu? '))
ano = int(input(' Nasceu em que ano? '))
dataNasc = datetime.date(ano, mes, dia)

# Diferenca de data atual e de data de nascimento
diff = (date.today() - dataNasc)

# Calculo do resultado
result = (diff.days / 365.25)

# Formata string, onde %d torna numero inteiro
print('\n Voce tem %d anos' %(result))
