nome = 'Carol Alves'
altura = 1.58
peso = 64
imc = peso / (altura * altura)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

# f-strings
print(linha_1)
print(linha_2)
print(linha_3)

# Carol Alves tem 1.58 de altura
# pesa 64 quilos e seu IMC é
# 25.64
