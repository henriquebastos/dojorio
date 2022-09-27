def soma(a,b):
	return a+b

def verificaSoma(a,b):
	return a+b > 9
	
def contaDigito(a):	
	return len(str(abs(a)))
	
def NumeroParaArray(a):
	b = list(str(abs(a)))
	for i,z in enumerate(b):
		b[i] = int(z)
	return b
	
def SomaArray(a,b):
	a_arr = NumeroParaArray(a)
	b_arr = NumeroParaArray(b)
	return a_arr[0]+b_arr[0]
	
	
	