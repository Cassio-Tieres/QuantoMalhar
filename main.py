def malhar(idade, peso):  # Função com as condicionais utilizadas no sistema.

    if idade < 28:
        peso = peso - 2

    else:
        peso = peso - 1

    return peso


# Recebimento dos dados do usuário para o cálculo.
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
peso_atual = float(input('Digite o seu peso atual: '))
qnt_quer = float(input('Digite sua meta: '))

vezesMalhou = 0

# Este código repetirá e somará quantas vezes o usuário terá que malhar.
while peso_atual > qnt_quer:
    peso_atual = malhar(idade, peso_atual)
    vezesMalhou = vezesMalhou + 1

print(f'{nome}, você precisa malhar {vezesMalhou} para chegar a sua meta')

