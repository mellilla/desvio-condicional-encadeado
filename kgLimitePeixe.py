# VALORES
peso_reg = 50 # peso máximo
multa_kg = 4.00 # por cada quilo excedente
bonificacao = 1.00 # por cada quilo pescado

# entrada
peso_peixes = float(input())

# calculos
if peso_peixes > peso_reg:
    excesso = peso_peixes - peso_reg
    multa = excesso * multa_kg
    print(f'{excesso: .2f}')
    print(f'{multa: .2f}')
else:
    bonificacao = peso_peixes * bonificacao
    print(f'{bonificacao: .2f}')