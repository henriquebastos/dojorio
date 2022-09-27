def checksum(account):
    return sum((i+1) * int(alg) for i, alg in enumerate(reversed(str(account)))) % 11

def check_account(account):
    return checksum(account) == 0
    
def ocr(entrada, validate=False):
    contas_lidas = []
    contas = _split_contas(entrada)
    for conta in contas:
        digitos = _split_digitos(conta)
        conta_lida = "".join(_ocr_digito(digito) for digito in digitos)
        if validate:
            if '?' in conta_lida:
                conta_lida += ' ILL'
            elif not check_account(conta_lida):
                conta_lida += ' ERR'
        contas_lidas.append(conta_lida)
    return '\n'.join(contas_lidas)

def _split_digitos(digitos):
    linhas = digitos.split('\n')
    numero_caracteres = len(linhas[0])

    return [
        "\n".join(
            [linhas[0][i : i + 3], linhas[1][i : i + 3], linhas[2][i : i + 3]]
        )
        for i in range(0, numero_caracteres, 3)
    ] 
    
def _split_contas(entrada):
    linhas = entrada.split('\n')
    numero_de_linhas = len(linhas)

    return ['\n'.join(linhas[i:i+3]) for i in range(0, numero_de_linhas, 4)]
    
def _ocr_digito(entrada):
    table = {'''\
 _ 
| |
|_|''': '0','''\
   
  |
  |''': '1', '''\
 _ 
 _|
|_ ''': '2', '''\
 _ 
 _|
 _|''': '3', '''\
   
|_|
  |''': '4', '''\
 _ 
|_ 
 _|''': '5', '''\
 _ 
|_ 
|_|''': '6', '''\
 _ 
  |
  |''': '7', '''\
 _ 
|_|
|_|''': '8', '''\
 _ 
|_|
 _|''': '9'}

    return table.get(entrada, '?')