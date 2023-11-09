from hashlib import sha256

def criptografar(chaveSecreta, senha):
    senha+=chaveSecreta
    # Soma-se a senha à chave secreta para torná-la ainda mais única

    senhaCriptografada = sha256(senha.encode())
    # Transformamos a senha em bytes usando o encode()
    # e a transformamos em um hash usando o método sha256

    return senhaCriptografada.hexdigest()
    # Retornamos o hash da senha criptografada, convertido em hexadecimal
    # para melhor visualização e manipulação
