def criptografar(chaveSecreta, senha):
    senhaCriptografada = ""
    # Inicializamos a string vazia para podermos a manipular
    tamanho = int(len(chaveSecreta))
    # Declaramos o tamanho da chave secreta
    
    for x, caractere in enumerate(senha):
    # Percorremos um a um os caracteres da senha
        novoCaractere = ord(caractere) + ord(chaveSecreta[x % tamanho])
        # Transformamos os caracteres em um conjunto numérico representado pela
        # soma do valor inteiro do caractere em questão da senha e o caractere 
        # simétrico da chave.
        senhaCriptografada+=str(novoCaractere)+"_"
        # Separa os conjuntos numéricos com um "_"

    return senhaCriptografada[:-1]
    # Retorna a senha criptografada, anulando o último separador

def descriptografar(chaveSecreta, senhaCriptografada):
    senhaOriginal = ""
    # Pegamos uma string vazia
    tamanho = int(len(chaveSecreta))

    senhaCriptografada = senhaCriptografada.split("_")
    # Removemos as divisórias entre os caracteres

    for x, caractere in enumerate(senhaCriptografada):
    # Percorremos um a um os caracteres da senha
        caractereOriginal = chr(int(caractere) - ord(chaveSecreta[x % tamanho]))
        # Encontramos o caractere original subtraindo o valor do
        # caractere respectivo da chave ao caractere da senha criptografada
        senhaOriginal+=str(caractereOriginal)
    
    return senhaOriginal
