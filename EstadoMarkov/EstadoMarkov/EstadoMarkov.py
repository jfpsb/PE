# José Felipe Silva Borges

# Atividade sobre estados da cadeia de markov

# Classe que representa um estado na cadeia de Markov
class Estado:
	def __init__(self, id):
		self.id = id
		self.acessiveis = []
		self.comunicantes = []
		self.absorvente = False
		self.recorrente = False
		self.transiente = False
		
	def isAbsorvente(self):
		return len(self.acessiveis) == 0
		
	def isRecorrente(self):
		return len(self.comunicantes) > 0
		
	def isTransiente(self):
		return self.isAbsorvente() == False and self.isRecorrente() == False
		
	def getClassificacao(self):
		if self.isAbsorvente():
			return "Absorvente"
		elif self.isRecorrente():
			return "Recorrente"
		else:
			return "Transiente"

# Classe que representa uma classe na cadeia de Markov	
class Classe:
	def __init__(self):
		self.estados = []
		
	def isRecorrente(self):
		for i in self.estados:
			if i.isRecorrente() == False:
				return False
		return True
		
	def isAbsorvente(self):
		for e in self.estados:
			for c in e.acessiveis:
				if c not in self.estados:
					return False
		return True
		
	def isTransiente(self):
		if len(self.estados) == 1 and len(self.estados[0].acessiveis) > 0:
			return True
		return False
		
	def getClassificacao(self):
		if self.isRecorrente():
			return "Recorrente";
		elif self.isTransiente():
			return "Transiente"
		else:
			return "Absorvente"

# Classe que representa a cadeia de Markov
class CadeiaDeMarkov:	
	# Checa se matriz é markoviana
	def isMatrizMarkoviana(self, matriz):
		for linha in matriz:
			soma = 0.0		
			for coluna in linha:
				soma += float(coluna)
			if soma != 1.0:
				return False	
		return True

	def getAcessiveis(self, E, v, visitado):
		visitado[v] = True	
		for i in range(E):
			if matriz[v][i] != 0.0 and visitado[i] == False:
				self.getAcessiveis(E, i, visitado)
				
	def populaAcessiveis(self):
		for y in range(self.E):
			visitado = [False] * self.E		
			self.getAcessiveis(self.E, y, visitado)
			self.matrizAcessiveis.append(visitado)
		
		for w in range(self.E):
			for j in range(self.E):
				if w != j and self.matrizAcessiveis[w][j] == True:
					self.estados[w].acessiveis.append(Estado(j))
					

				
	def populaComunicantes(self):
		for i in range(0, len(self.matrizAcessiveis)):
			for j in range(i, len(self.matrizAcessiveis)):
				if i != j:
					if self.matrizAcessiveis[i][j] == True and self.matrizAcessiveis[j][i] == True:
						self.estados[i].comunicantes.append(Estado(j))
						self.estados[j].comunicantes.append(Estado(i))
	
	# Atribui classes na cadeia
	def populaClasses(self):
		visitado = [False] * len(self.estados)
		
		for e in self.estados:
			if visitado[e.id] == False:
				visitado[e.id] = True;
				classe = Classe()
				
				classe.estados.append(e)
				
				for i in e.comunicantes:
					classe.estados.append(i)
					visitado[i.id] = True
				
				self.classes.append(classe)
				
	def printEstados(self):
		for e in self.estados:
			output = ">>> Estado {}: {}"
			print(output.format(e.id, e.getClassificacao()))
			
	def printTipoClasses(self):
		i = 1
		for c in self.classes:
			output = "Classe {}: {}"
			print(output.format(i, c.getClassificacao()))
			i += 1
			
	def printAcessiveis(self):
		print(">>> Estados Acessíveis")
		for e in self.estados:
			for a in e.acessiveis:
				output = "\t{} --> {}"
				print(output.format(e.id, a.id))
				
	def printComunicantes(self):
		print(">>> Estados Comunicantes")
		dic = {}
		for e in range(self.E):
			dic[e] = []
		for e in self.estados:
			for a in e.comunicantes:
				if e.id not in dic[a.id] and a.id not in dic[e.id]:
					output = "\t{} <--> {}"
					print(output.format(e.id, a.id))
					dic[e.id].append(a.id)
					dic[a.id].append(e.id)
					
	def printClasses(self):
		print(">>> Classes")
		for c in range(0, len(self.classes)):
			output = "\tClasse {}: "
			print(output.format(c + 1), end = '')
			for e in self.classes[c].estados:
				print(str(e.id) + " ", end = '')
			print()
			
	def isRedutivel(self):
		if len(self.classes) == 1:
			return "Irredutível"
		else:
			return "Redutível"
			
	def isRegular(self):
		for i in range(self.E):
			for j in range(self.E):
				if matriz[i][j] == 0.0:
					return "Irregular"
		return "Regular"
	
	def __init__(self, matriz):
		self.estados = []
		self.classes = []
		self.matrizAcessiveis = []
		self.matriz = matriz
		self.E = 0
		
		if self.isMatrizMarkoviana(matriz):		
			for i in range(0, len(matriz)):
				self.estados.append(Estado(i))
				
			self.E = len(self.estados)
			self.populaAcessiveis()
			self.populaComunicantes()
			self.populaClasses()
			
			print(">>> A Cadeia É " + self.isRedutivel())
			print(">>> A Cadeia É " + self.isRegular())
			self.printEstados()
			self.printAcessiveis()
			self.printComunicantes()
			self.printClasses()
			self.printTipoClasses()
		else:
			print("Matriz não é markoviana")

# Se quiser informar a matriz através do console, marque como True
_MATRIZ_PELO_CONSOLE = False

matriz = [[0.0, 1.0, 0.0, 0.0, 0.0],
		  [1.0, 0.0, 0.0, 0.0, 0.0],
		  [0.0, 0.0, 1.0, 0.0, 0.0],
		  [0.0, 0.0, 1.0, 0.0, 0.0],
		  [1.0, 0.0, 0.0, 0.0, 0.0]]
	
			
# Executando
if _MATRIZ_PELO_CONSOLE:
	matriz.clear()
	
	print("Informe o tamanho do espaço de estados: ")
	EE = int(input())
	
	txtElementosMatriz = "Informe as {} probabilidades da matriz markoviana (separados por espaço): "
	elementosMatriz = EE ** 2
	print(txtElementosMatriz.format(elementosMatriz))
	
	prob = input().split(" ")
	
	# Converte de string para float
	prob = [float(i) for i in prob]
	
	inicio = 0
	fim = EE
	
	for x in range(EE):
		matriz.append(prob[inicio:fim])
		inicio += EE
		fim += EE
		
	print(matriz)

# Instancia cadeia
CadeiaDeMarkov(matriz)
