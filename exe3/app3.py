from datetime import datetime, timedelta
# Importante pois mais para frente validaremos a data atual
print("Seja bem-vindo(a), colaborador(a)! Insira seus dados abaixo!")

nome = str(input("Seu nome: "))

dataAdmissao = str(input("Sua data de admissão: "))
if datetime.strptime(dataAdmissao, "%d/%m/%Y") > datetime.today() - timedelta(days=5*365):    
    print(f"Caro(a) {nome}, ")
    print("Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa.")
    exit()
# Aqui já verificamos se o colaborador se enquadra no requisito mínimo de participação do
# programa e se não, já abortamos a execução

salario = float(input("Salário atual: "))

while True:
# Laço para prender o usuário até que este insira um valor válido
    try:
    # Tratamento de exceções para impedir que inserir caracteres ou letras não
    # interrompa a execução
        emprestimo = int(input("Valor do empréstimo: "))
    except ValueError:
        print("Insira um valor válido!")
    else:
        if emprestimo % 2 == 0 and emprestimo <= salario * 2:
        # Requisitos para solicitar um empréstimo
            break
        print("Insira um valor válido!")
        # Se o loop não encerrar no break, significa que o valor não corresponde
        # aos requisitos esperados. Decidi não colocar a cláusula 'else'

def maiorValor(valor):
# Função que divide o valor do empréstimo em notas maiores
# A fórmula geral é: 
# Quantidade de notas (quociente), valor restante (resto) = valor atual / valor da nota
    if valor >= 100:
        notasCem, resto = divmod(valor, 100)
        print(f"{notasCem} x 100 reais;")
    if resto >= 50:
        notasCinquenta, resto = divmod(resto, 50)
        print(f"{notasCinquenta} x 50 reais;")
    if resto >= 2:
        menorValor(resto)
    
def menorValor(valor):
    if valor >= 20:
        notasVinte, resto = divmod(valor, 20)
        print(f"{notasVinte} x 20 reais;")
    if resto >= 10:
        notasDez, resto = divmod(resto, 10)
        print(f"{notasDez} x 10 reais;")
    if resto >= 5:
        notasCinco, resto = divmod(resto, 5)
        print(f"{notasCinco} x 5 reais;")
    if resto >= 2:
        notasDois = resto // 2
        print(f"{notasDois} x 2 reais;")

def exibir(v1, v2):
# Esta função foi criada apenas para não repetir métodos de exibição
    print(f"{v1} em notas de maior valor:")
    maiorValor(v1)
    print(f"\n{v2} em notas de menor valor:")
    menorValor(v2)
    return


print(f"\n{nome}, as suas opções são:\n")
exibir(emprestimo, emprestimo)
print("\nNotas meio a meio:")
exibir(emprestimo//2, emprestimo//2)