import asci, sha256, fernet
# Separei as criptografias em arquivos para ficar mais fácil de identificar

chave = "#modalGR#GPTW#top#maiorEmpresaTecnologia#baixadaSantista"
# Chave secreta para criptografia

senhas = ['AmoSucoDeUva', 'PythonMelhorQueJava', 'EuSouModal']
# Exemplos de senhas

senha1 = asci.criptografar(chave, senhas[0])
senha2 = sha256.criptografar(chave, senhas[1])
senha3 = fernet.criptografar(chave, senhas[2])
# Todos os arquivos possuem uma função criptografar() que recebe
# como parâmetro a chave e uma das senhas, e retorna a versão
# codificada da mesma.

print(f"Senha 1 criptografada em ASCII: {senha1}")
print(f"Senha 2 criptografada em SHA256: {senha2}")
print(f"Senha 3 criptografada em Fernet: {senha3}")