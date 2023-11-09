from cryptography.fernet import Fernet
import base64
# from hashlib import md5

def filtrarChave(chave):
    # Tenho duas maneiras para conseguir isso:

    # Método 1: Hashing usando MD5, que nos gera exatos 32 caracteres hexadecimais,
    # o que facilita a sua conversão para base64, além de o processo de hashing
    # fornecer uma proteção extra à chave secreta, principalmente para métodos de descriptografia.
    ''' 
    chaveAjustada = md5(chave.encode()).hexdigest()
    '''


    # Método 2: Ajustar a chave a 32 caracteres
    # Nesse caso em específico, a chave secreta possui 44 bits, o que dificulta o
    # processo de transformação em uma chave válida para o Fernet (método de criptografia
    # escolhido). Sendo assim, criei esse pequeno algoritmo para ajustar a chave
    if len(chave) < 32:
        chaveAjustada = chave.ljust(32, 'A')  
        # Preenche a string até atingir 32 caracteres
    else:
        chaveAjustada = chave[:32]
        # Reduz a string aos seus primeiros 32 caracteres
    

    return chaveAjustada



def criptografar(chaveSecreta, senha):
    chaveSecreta = filtrarChave(chaveSecreta)
    # Primeiramente, nós precisamos transformar a chave secreta em algo
    # de 32 caracteres de base64 "url safe", isso porque alguns caracteres 
    # de base64 não são seguros para uso em URLs sendo assim, 

    chaveSecreta = base64.b64encode(chaveSecreta.encode())
    # Codifica a chave, agora com 32 dígitos, em base64

    chaveFernet = Fernet(chaveSecreta)
    # Inicializa o objeto Fernet com a chave_secreta anteriormente,
    # possibilitando que usemos os métodos encrypt() e decrypt() agora
   
    senhaCriptografada = chaveFernet.encrypt(senha.encode())
    # Criptografa a nossa senha simetricamente usando a nossa chave secreta

    return(senhaCriptografada.decode())

def descriptografar(chaveSecreta, senhaCriptografada):
    # O processo não difere muito da criptografia:
    
    chaveSecreta = filtrarChave(chaveSecreta)
    # Ajustamos a chave para atender aos padrões do Fernet

    chaveSecreta = base64.b64encode(chaveSecreta.encode())
    # Codificamos a chave

    chaveFernet = Fernet(chaveSecreta)
    # Inicializamos o objeto

    senhaOriginal = chaveFernet.decrypt(senhaCriptografada.encode())
    # Criptografa a nossa senha simetricamente usando a nossa chave secreta

    return(senhaOriginal.decode())
