def ocr(entrada):
    digitos = split_digitos(entrada)
    saida = "".join(ocr_digito(digito) for digito in digitos)
    return int(saida)

def split_digitos(digitos):
    linhas = digitos.split('\n')
    numero_caracteres = len(linhas[0])

    return [
        "\n".join(
            [linhas[0][i : i + 3], linhas[1][i : i + 3], linhas[2][i : i + 3]]
        )
        for i in range(0, numero_caracteres, 3)
    ] 
    
def ocr_digito(entrada):
    table = {'''\
   
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

    return table[entrada]

     
     

    
