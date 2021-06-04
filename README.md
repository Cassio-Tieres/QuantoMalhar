# QuantoMalhar

Este código tem como objetivo calular quantas vezes você tem que malhar para alcançar o seu peso desejado. Inicialmente, 
a ideia do código veio em um exercício em portugol, porém, tentei refazer utilizando python e depois de muito estudar, consegui concluir.

# Criação:
1º Passo: Criei uma função, chamada malhar, para que ela armazenasse a estrutura condicional que seria usada no sistema.

2º Criei as variáveis com nomes intuitivos que seriam de fácil compreensão para que qualquer pessoa entenda do que se trata. Abaixo está o dicionário de variáveis usadas no código.

<ul> nome = recebe o nome do usuário.
<ul> idade = recebe a idade do usuário.
<ul> peso_atual = vai receber o peso atual do usuário. Este será usado no cálculo.
<ul> qnt_quer = recebe o peso/meta do usuário. Também será usado no cálculo.
<ul> vezesMalhou = recebe 0 no iníciou, será usado para receber o cálculo do peso_atual e qnt_quer. Este aparecerá para o cliente.
    
3º While: O while foi utilizado usando a lógica do método chinês. Ele irá repetir o cálculo até que "peso_atual" fique < ( menor que ) "qnt_quer".

# Modo de usar:
                                                                                                                          
<ul> 1º passo: Usuário deve escrever seu nome.
<ul> 2º passo: Usuário deve escrever sua idade.
<ul> 3º passo: Usuário deve escrever o seu peso atual.
<ul> 4º passo: Usuário deve escrever a sua meta.

Após os dados serem preenchidos, o código irá fazer todo o trabalho em relação ao cálculo. O resultado de tudo será printado ( impresso ) para o cliente.



Vale salientar que: no print(), ao invés de utilizar "f" para interpolar, também pode-se usar o format(). Assim:
print('{0}, você precisa malhar {1} x para chegar a sua meta.'.format({nome}, {vezesMalhou}))
