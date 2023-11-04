from datetime import date
mes = date.today().month
# Imprescindível para obtermos o mês em questão!

caminhoFonte = "exe2/fonteExe2.txt"
# Deposite aqui o caminho do arquivo fonte da Modal.

print(f"Você está prestes a filtrar os aniversariantes do mês {mes} no arquivo localizado em '{caminhoFonte}' !")
input("Aperte [ENTER] para continuar...")
# Por mais simples que o programa seja, deve-se ter em mente que ele está 
# sendo desenvolvido para terceiros, que podem ou não entender de programação,
# logo, interação instrutiva nunca é demais.

with open(caminhoFonte) as arquivoFonte:
    linhas_filtradas = [linha for linha in arquivoFonte if int(linha.split("/")[1]) == mes]
    # Coleta apenas as linhas cuja data de nascimento seja do mês vigente
    
with open("exe2/resultadoExe2.txt", "w") as arquivoResposta:
    arquivoResposta.writelines(linha for linha in linhas_filtradas)
    # Adiciona ao arquivo resposta apenas os dados filtrados anteriormente

print("Resultado criado com sucesso!")