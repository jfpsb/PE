### Declarações
# Se quiser informar a matriz através do console, marque como True
_MATRIZ_PELO_CONSOLE = False

matriz = [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
		  [1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
		  [0.5, 0.5, 0.0, 0.0, 0.0, 0.0],
		  [0.25, 0.25, 0.25, 0.0, 0.25, 0.0],
		  [0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
		  [0.0, 0.0, 0.0, 0.0, 1.0, 0.0]]
		  
# Tamanho do espaço de estados
E = len(matriz)
		  
# Matriz que guarda se um estado é acessível por outro
matrizAcessibilidade = []

### Funções
# Checa se matriz é markoviana
def isMatrizMarkoviana(matriz):
	for linha in matriz:
		soma = 0
		
		for coluna in linha:
			soma += coluna
			
		if soma != 1.0:
			return False
	
	return True
	
# Função que retorna os estados acessíveis de um estado
def isAcessivel(E, v, visitado):
	visitado[v] = True	
	for i in range(E):
		if matriz[v][i] != 0.0 and visitado[i] == False:
			isAcessivel(E, i, visitado)
			
# Função que chama isAcessivel para cada estado
def populaMatrizAcessiveis():
	for i in range(E):
		visitado = [False] * E		
		isAcessivel(E, i, visitado)
		matrizAcessibilidade.append(visitado)
			
# Função que imprime os estados acessíveis
def printAcessiveis(matrizAcessibilidade):
	print(">>> Estados Acessíveis")
	print("\t#estado --> estado")
	for i in range(0, len(matrizAcessibilidade)):
		for j in range(0, len(matrizAcessibilidade)):
			if i != j and matrizAcessibilidade[i][j] == True:
				output = "\t{} --> {}"
				print(output.format(i, j))
	
# Função que imprime os estados comunicantes	
def printComunicantes(matrizAcessibilidade):
	dic = {}
	print(">>> Estados Comunicantes")
	print("\t#estado <--> estado")
	for i in range(0, len(matrizAcessibilidade)):
		for j in range(0, len(matrizAcessibilidade)):
			if i != j:
				if matrizAcessibilidade[i][j] == True and matrizAcessibilidade[j][i] == True:
					if i not in dic and j not in dic:
						output = "\t{} <--> {}"
						print(output.format(i, j))
						dic[i] = j
						dic[j] = i

# Executando
if _MATRIZ_PELO_CONSOLE:
	matriz.clear()
	
	print("Informe o tamanho do espaço de estados: ")
	E = int(input())
	
	txtElementosMatriz = "Informe as {} probabilidades da matriz markoviana (separados por espaço): "
	elementosMatriz = E ** 2
	print(txtElementosMatriz.format(elementosMatriz))
	
	prob = input().split(" ")
	
	inicio = 0
	fim = E
	
	for x in range(E):
		matriz.append(prob[inicio:fim])
		inicio += E
		fim += E

if isMatrizMarkoviana(matriz):
	populaMatrizAcessiveis()
	printAcessiveis(matrizAcessibilidade)
	printComunicantes(matrizAcessibilidade)
else:
	print("Matriz não é Markoviana")
