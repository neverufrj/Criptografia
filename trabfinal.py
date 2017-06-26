#Bibliotecas utilizadas
import random
import os.path
#Demais algoritmos
def MDC(n1,n2):
	number1 = n1
	number2 = n2
	q = 0
	r = 0
	while(number2 != 0):
		r = number1%number2
		q = number1/number2
		number1 = number2
		number2 = r
	return number1
def ExpModular(b,e,m):
	result = 1
	base = b
	exponent = e
	module = m
	while(exponent != 0):
		if(exponent % 2 == 0):
			exponent /= 2
			base *= base
			base = base%module
		else:
			exponent = (exponent-1)/2
			result= (result*base)%module
			base *= base
			base = base%module
	return result
def MillerRabin(number,base):
	n = number
	b = base
	if(n % 2 == 0 and n != 2):
		return "Composto"
	elif(n == 1 or n == 2 or n == 3):
		return "Primo"
	else:
		k = 0
		q = n - 1
		while(q % 2 == 0):
			k += 1
			q /= 2
		t = ExpModular(b,q,n)
		if(t == 1 or t == n-1):
			return "Primo"
		else:
			i = 1
			while (i < k):
				t = ExpModular(t,2,n)
				if(t == n-1):
					return "Primo"
				else:
					i += 1
			return "Composto"
def EuclidianoEstendido(n1,n2):
	number1 = n1
	number2 = n2
	q = 0
	r = 0
	savedX = 0
	x1 = 1
	x2 = 0
	y1 = 0
	y2 = 1
	while(number2 != 0):
		r = number1 % number2
		q = number1/number2
		number1 = number2
		number2 = r
		temp = y1
		temp -= (y2*q)
		y1 = y2
		y2 = temp
		temp = x1
		temp -= (x2*q)
		x1 = x2
		x2 = temp
		if(number2 != 0):
			savedX = x2
	return savedX;
def ConvertToHex(decimal):
    n = (decimal % 16)
    temp = ""
    if (n < 10):
        temp = n
    if (n == 10):
        temp = "A"
    if (n == 11):
        temp = "B"
    if (n == 12):
        temp = "C"
    if (n == 13):
        temp = "D"
    if (n == 14):
        temp = "E"
    if (n == 15):
        temp = "F"
    if (decimal - n != 0):
        return ConvertToHex(decimal / 16) + str(temp)
    else:
        return str(temp)
def ConvertToDec(hexadecimal):
	n = hexadecimal
	result = int(n,16)
	return str(result)
def Module(n,m):
	result = 0
	num = n
	mod = m
	if(num < 0):
		num *= -1
		if(num < mod):
			result = mod - num
		else:
			result = num%mod
	else:
		result = num%mod
	return result
def AlgoritmoIngenuo(number):
	n = number
	f = int(number ** 0.5)
	initial = 2
	repeat = 0
	numbers = []
	expoents = []
	while(n != 1 and initial <= f):
		if(n % initial == 0):
			n = n/initial
			repeat += 1
			if(n % initial != 0):
				numbers.append(initial)
				expoents.append(repeat)
		if(n % initial != 0):
			repeat = 0
			initial += 1
	return numbers, expoents
def AlgoritmoDeGauss(listNum, listExp, number):
	n = number
	listN = listNum
	listE = listExp
	i = 0
	g = 1
	k = len(listN)
	while(i < k):
		a = 2
		while((ExpModular(a,((n-1)/listN[i]),n)) == 1):
			a += 1
		h = ExpModular(a,(n-1)/(ExpModular(listN[i],listE[i],n)), n)
		g = (g * h) % n
		i += 1
	return g
def FindGenerator(g, number):
	m = 1
	n = number
	generator = g
	c = 0
	stop = False
	while(stop == False):
		if(EuclidianoEstendido(m, n-1) == 1):
			temp = (generator**m)%n
			if(temp != g):
				c = temp
				stop = True
		m += 1
	return c
def Phi(n):
	number = n
	c = 0
	divisor = 1
	auxN = 0
	auxD = 0
	resto = 0
	stop = False
	while(divisor < number and stop == False):
		auxN = number
		auxD = divisor
		resto = 1
		while(resto != 0):
			resto = auxN%auxD
			if(resto == 0):
				if(auxD == 1 and divisor != 1):
					c = divisor
					stop = True
				divisor += 1
			else:
				auxN = auxD
				auxD = resto
	return c
#-----------------------------------------------------------------------------------------------------------------------------
#Metodos para o modo de geracao de chaves
def SaveKeys(n,e,d):
	chose = ''
	while(chose != "Salvar" and chose != "Exibir"):
		print("Deseja 'Salvar' ou 'Exibir' no terminal as chaves e componentes gerados?")
		chose = raw_input()
		if(chose == "Salvar"):
			print("Voce escolheu 'Salvar' as chaves e componentes gerados.")
			print("")
			publicF = open("ChavePublica", 'w')
			publicF.write(n + "\n")
			publicF.write(e + "\n")
			privateF = open("ChavePrivada", 'w')
			privateF.write(n + "\n")
			privateF.write(d + "\n")
			print("Arquivo salvo com sucesso!")
		elif(chose == "Exibir"):
			print("Voce escolheu 'Exibir' as chaves e componentes gerados.")
			print("")
			print("Chave Publica:")
			print(n)
			print(e)
			print("Chave Privada:")
			print(n)
			print(d)
		else:
			print("Entrada invalida, tente novamente.")
			print("")
def GRSA():
	p = 10
	q = 10
	while(MillerRabin(p,2) != "Primo"):
		p = random.getrandbits(128)
	while(MillerRabin(q,2) != "Primo"):
		q = random.getrandbits(128)
	n = p*q
	phiN = (p-1)*(q-1) #ate aqui tudo beleza
	e = 2 #ate aqui beleza
	while(e < phiN and MDC(e,phiN) != 1):
		e += 1 #ate aqui beleza
	d = EuclidianoEstendido(e,phiN)
	if(d < 0):
		d = Module(d,phiN)
	else:
		d = d%phiN# ate aqui beleza
	e = ConvertToHex(e)
	d = ConvertToHex(d)
	n = ConvertToHex(n) #ate aqui beleza
	while(len(e) < 64): #aumentar o hexadecimal se ele estiver com 31 numeros
		e = "0"+e
	while(len(d) < 64):
		d = "0"+d
	while(len(n) < 64):
		n = "0"+n
	print("Chaves geradas com sucesso!")
	print("")
	SaveKeys(n,e,d)


def GElGamal():
	q = 10
	p = 10
	b = 2
	print("Gerando chaves e componentes...")
	print("")
	while(MillerRabin(q,2) != "Primo" or MillerRabin(p,2) != "Primo" or q.bit_length() != 255 or p.bit_length() != 256):
		q = random.getrandbits(255)
		p = q*2+1
	while(ExpModular(b, q, p) == 1):
		b += 1
	g = b
	c = Phi(p)
	a = 2
	while(ExpModular(g, a, p) != c and a < p-1):
		a += 1
	print(p)
	print(g)
	print(c)
	print(a)


def GCriptografia():
	chose = ''
	while(chose != "RSA" and chose != "El Gamal"):
		print("Voce deseja gerar chaves para 'RSA' ou para 'El Gamal'?")
		chose = raw_input()
		if(chose == "RSA"):
			print("Voce escolheu gerar chaves para RSA.")
			print("")
			GRSA()
		elif(chose == "El Gamal"):
			print("Voce escolheu gerar chaves para El Gamal.")
			print("")
			GElGamal()
		else:
			print("Entrada invalida, tente novamente.")
			print("")

#Programa principal de geracao de chaves
def Gprogram():
	chose = ''
	while(chose != "Assinatura Digital" and chose != "Criptografia"):
		print("Voce deseja gerar uma 'Assinatura Digital' ou chaves de 'Criptografia'?")
		chose = raw_input()
		if(chose == "Criptografia"):
			print("Voce escolheu gerar chaves de Criptografia.")
			print("")
			GCriptografia()
		elif(chose == "Assinatura Digital"):
			print("Voce escolheu gerar uma Assinatura Digital.")
			print("")

		else:
			print("Entrada invalida, tente novamente.")
			print("")
#-----------------------------------------------------------------------------------------------------------------------------
#Metodos para o modo de encriptacao (pura)
def ERSA(fName):
	chose = ''
	n = 0
	e = 0
	while(chose != "Digitar" and chose != "Leia"):
		print("Voce deseja 'Digitar' ou deseja que o programa 'Leia' a chave publica de um arquivo?")
		chose = raw_input()
		if(chose == "Digitar"):
			print("Voce escolheu digitar a chave publica do RSA.")
			print("")
			n = raw_input()
			e = raw_input()
		elif(chose == "Leia"):
			print("Voce escolheu ler a chave publica do RSA de um arquivo.")
			print("")
			fileOK = False
			chosef = ''
			while(fileOK == False):
				print("Qual o nome do arquivo que contem a chave publica para encriptar?")
				chosef = raw_input()
				if(os.path.exists(chosef)):
					print("Arquivo encontrado!")
					print("")
					fileOK = True
					publicF = open(chosef, 'r')
					n = publicF.readline()
					e = publicF.readline()
					n = n[:-1]
					e = e[:-1]
				else:
					print("Arquivo nao existe, tente novamente.")
					print("")
		else:
			print("Entrada invalida, tente novamente.")
			print("")
	primaryF = open(fName,'r')
	content = primaryF.read()
	c = 0
	print("Escolha o nome do arquivo quando encriptado:")
	nameF = raw_input()
	newF = open(nameF, 'w')
	block = ''
	print("")
	print("Encriptando...")
	while(c < len(content)):
		block = (ord(content[c])+100)
		block = ExpModular(block, int(ConvertToDec(e)), int(ConvertToDec(n)))
		newF.write(str(block)+"\n")
		c += 1
	print("Arquivo encriptado com sucesso!")
def EElGamal(fName):
	print()
	print()
#Programa principal de encriptacao
def Eprogram():
	chose = ''
	chosef = ''
	fileOK = False
	while(chose != "RSA" and chose != "El Gamal"):
		print("Voce deseja encriptar com 'RSA' ou com 'El Gamal'?")
		chose = raw_input()
		if(chose == "RSA"):
			print("Voce escolheu encriptar com RSA.")
			print("")
		elif(chose == "El Gamal"):
			print("Voce escolheu encriptar com El Gamal.")
			print("")
		else:
			print("Entrada invalida, tente novamente.")
			print("")
	while(fileOK == False):
		print("Qual o nome do arquivo que voce deseja encriptar?")
		chosef = raw_input()
		if(os.path.exists(chosef)):
			print("Arquivo encontrado!")
			print("")
			fileOK = True
			if(chose == "RSA"):
				ERSA(chosef)
			else:
				EElGamal(chosef)
		else:
			print("Arquivo nao existe, tente novamente.")
			print("")
#-----------------------------------------------------------------------------------------------------------------------------
#Metodos para o modo de decriptacao (pura)
def DRSA(fName):
	chose = ''
	n = 0
	d = 0
	while(chose != "Digitar" and chose != "Leia"):
		print("Voce deseja 'Digitar' ou deseja que o programa 'Leia' a chave privada de um arquivo?")
		chose = raw_input()
		if(chose == "Digitar"):
			print("Voce escolheu digitar a chave privada do RSA.")
			print("")
			n = raw_input()
			d = raw_input()
		elif(chose == "Leia"):
			print("Voce escolheu ler a chave privada do RSA de um arquivo.")
			print("")
			fileOK = False
			chosef = ''
			while(fileOK == False):
				print("Qual o nome do arquivo que contem a chave privada para decriptar?")
				chosef = raw_input()
				if(os.path.exists(chosef)):
					print("Arquivo encontrado!")
					print("")
					fileOK = True
					publicF = open(chosef, 'r')
					n = publicF.readline()
					d = publicF.readline()
					n = n[:-1]
					d = d[:-1]
				else:
					print("Arquivo nao existe, tente novamente.")
					print("")
		else:
			print("Entrada invalida, tente novamente.")
			print("")
	primaryF = open(fName,'r')
	print("Escolha o nome do arquivo quando decriptado:")
	nameF = raw_input()
	newF = open(nameF, 'w')
	line = primaryF.readline()
	print("")
	print("Decriptografando...")
	while(line != ''):
		block = line
		block = ExpModular(int(block), int(ConvertToDec(d)), int(ConvertToDec(n)))
		block = chr((int(block)-100))
		newF.write(block)
		line = primaryF.readline()
	print("Arquivo decriptografado com sucesso!")
def DElGamal(fName):
	print()
def Dprogram():
	chose = ''
	chosef = ''
	fileOK = False
	while(chose != "RSA" and chose != "El Gamal"):
		print("Voce deseja decriptar com 'RSA' ou com 'El Gamal'?")
		chose = raw_input()
		if(chose == "RSA"):
			print("Voce escolheu decriptar com RSA.")
			print("")
		elif(chose == "El Gamal"):
			print("Voce escolheu decriptar com El Gamal.")
			print("")
		else:
			print("Entrada invalida, tente novamente.")
	while(fileOK == False):
		print("Qual o nome do arquivo que voce deseja decriptar?")
		chosef = raw_input()
		if(os.path.exists(chosef)):
			print("Arquivo encontrado!")
			print("")
			fileOK = True
			if(chose == "RSA"):
				DRSA(chosef)
			else:
				DElGamal(chosef)
		else:
			print("Arquivo nao existe, tente novamente.")
			print("")

#-----------------------------------------------------------------------------------------------------------------------------
def program():
	chose = ""
	print("Bem vindo ao trabalho de final da disciplina de Numeros Inteiros e Criptografia da Universidade Federal do Rio de Janeiro.")
	print("")
	while(chose != '1' and chose != '2' and chose != '3' and chose != '4' and chose != '5' and chose != '6' and chose != '7'):
		print("Escolha um dos modos abaixo para comecar a utilizar o programa:")
		print("1 - Modo de geracao de chaves.")
		print("2 - Modo de encriptacao (pura).")
		print("3 - Modo de decriptacao (pura).")
		print("4 - Modo de assinatura digital (pura).")
		print("5 - Modo de verificacao de assinatura (pura).")
		print("6 - Modo de assinatura digital e encriptacao (combinados).")
		print("7 - Modo de decriptacao e verificacao de assinatura (combinados).")
		chose = raw_input()
		if(chose == '1'):
			print("Modo de geracao de chaves escolhido.")
			print("")
			Gprogram()
		elif(chose == '2'):
			print("Modo de encriptacao (pura) escolhido.")
			print("")
			Eprogram()
		elif(chose == '3'):
			print("Modo de decriptacao (pura) escolhido.")
			print("")
			Dprogram()
		elif(chose == '4'):
			print("Modo de assinatura digital (pura) escolhido.")
			print("")
		elif(chose == '5'):
			print("Modo de verificacao de assinatura (pura) escolhido.")
			print("")
		elif(chose == '6'):
			print("Modo de assinatura digital e encriptacao (combinados) escolhido.")
			print("")
		elif(chose == '7'):
			print("Modo de decriptacao e verificacao de assinatura (combinados) escolhido.")
			print("")
		else:
			print("Entrada invalida, tente novamente.")

program()
