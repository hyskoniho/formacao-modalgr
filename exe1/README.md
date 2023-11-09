# Exercício 1: Criptografias

Eis aqui a minha resolução ao exercício número 1, que propunha a utilização de três métodos de criptografia distintos que utilizassem de uma mesma chave secreta. Espero que apreciem as minhas soluções, pois eu me diverti bastante quebrando a cabeça para solucionar o problema do cofre! 😄

## Conteúdo

- [Visão Geral](#vis%C3%A3o-geral)
- [Requisitos](#requisitos)
- [Instalação](#instala%C3%A7%C3%A3o)
- [Observações](#observa%C3%A7%C3%B5)

## Visão Geral

A execução do projeto consiste em seu arquivo principal `app.py`, responsável por armazenar as senhas e a chave de segurança, bem como aplicá-las aos algoritmos de criptografia:
- `asci.py`
- `sha256.py`
- `fernet.py`
<br>
Cada um destes três algoritmos é responsável por um método de criptografia diferente.

#### ASCII:
Este algoritmo é bem simples, percorrendo a senha e transformando cada caractere em um conjunto de inteiros representado pela soma dos números relativos à *tabela ASCII* do caractere em questão e do caractere de igual posição na chave secreta.
Ele inclui as funções criptografar() e descriptografar(), que possuem funcionalidades reversas.

#### SHA-256:
O método em questão consegue ser o mais simples e o mais seguro, uma vez que utiliza da biblioteca *hashlib* para acessar a função do SHA-256, um metódo de criptografia extremamente popular por sua grande presença na maioria dos algoritmos vistos pela internet e sua robusta segurança. Seu método de criptografia consiste na criação de *hashs* de 32 bytes que são únicos e praticamente indecifáveis, uma vez que é impraticável a realização de engenharia-reversa ou ataques de força bruta (brute-force), bem extremamente resistentes à colisão (isto é, dificilmente será gerada a mesma combinação hash para dois valores distintos)  
Isso também significa que a criptografia por meio do SHA-256 é de via única e  não pode ser decifrada. Minha estratégia aqui foi concatenar o valor da chave secreta à senha escolhida, de modo a garantir a exclusividade da senha perante a colisões e a segurança intelectual da senha, uma vez que ela se torna bipartida (isto é, consistindo de um valor que é a senha e um valor que é constante, que é a chave, mas ainda assim secreto). Deste modo, este algoritmo se torna aplicável na situação proposta por meio da validação: o hospedeiro converte a senha e a chave secreta da tentativa de desbloqueio em hash usando o sha-256 e compara o valor obtido com o valor armazenado, uma vez que as hashs são únicas. Deste modo, mesmo que uma violação garanta o acesso ao valor da hash armazenada, ainda não seria possível a validação por meio da tentativa e conversão.

#### Fernet:
O *Fernet* é um esquema de criptografia simétrica, o que significa que a mesma chave é usada tanto para criptografar quanto para descriptografar os dados. O resultado desta criptografia contém os dados criptografados e informações adicionais, como um timestamp e um nonce (número usado apenas uma vez) para evitar a reutilização do token. Essas informações adicionais são importantes para evitar ataques de força bruta, uma vez que para a descriptografia, são verificados o *token* e as *time stamps*.

## Requisitos

- Python 3
- [cryptography](https://pypi.org/project/cryptography/)
- [base64](https://docs.python.org/3/library/base64.html#module-base64)
- [hashlib](https://docs.python.org/3/library/hashlib.html)
<br>Normalmente estas duas últimas vêm junto com o pip ao instalar o Python.

## Instalação

Clone o projeto para o seu computador
```bash
$ git clone https://github.com/hyskoniho/formacao-modalgr
```
</br>

Instale as bibliotecas necessárias<br></br>
No Windows:
```bash
pip install cryptography
```
No Linux/MacOS:
```bash
pip3 install cryptography
```

## Observações
No projeto, foram adicionadas as chaves e as senhas ao script apenas como meio de facilitar a execução de testes e representações do exercício, tenho plena consciência que em termos de segurança da informação, dados considerados críticos, como as senhas e a chave devem ser guardadas sob rigorosa segurança e privacidade.
