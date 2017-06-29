'''
UFRJ - Universidade Federal do Rio de Janeiro
Disciplina: Numeros inteiros e criptografia
Professor: Menasche
Nome: David Melo da Silva
DRE: 117079728
VeRSAgeradoro:0.2 (ATUALIZADA EM :27/06/2017)

26/06/2017 - menuprincipal criado
26/06/2017 - Modo de geracao de chaves

O programa elaborado para este trabalho devera ser capaz de encriptar e/ou assinar digitalmente
qualquer arquivo salvo no computador.
1-Em caso de realizacao de uma assinatura digital,o metodo utilizado sera o El Gamal.
2-Em caso de realizacao de criptografia o metodo utilizado sera entre RSAgerador ou El Gamal
de acordo com a escolha do usuario.

'''
from hashlib import sha224
import os.path
import random
import sys


#funcoes semente--------------------------------------------------
def hexparadec(hexadecimal): # colocar no menuprincipal
	num = hexadecimal
	divisao = int(num,16)
	return str(divisao)

def decparahex(decimal): #funcao que converte decimal para inteiro

    num = (decimal % 16)
    digitos = "0123456789ABCDEF"
    resto = decimal / 16
    if (resto == 0):
        return digitos[num]
    return decparahex(resto) + digitos[num]

def geradordeprimo(k): #gerador de primos
	ehprimo=False

	while(ehprimo==False):
		valor=random.getrandbits(128)
		ehprimo=millerrabin(valor)
		if ehprimo==True:
			primo=valor
	return primo


# exponenciacao modular
def expomod(base,expo,mod): #exponenciacao modular usada no millerabin
	R=1
	while expo!=0:
		if expo%2==1:
			R = (R*base)%mod
			expo=(expo-1)/2
		else:
			expo=expo/2
		base=(base*base)%mod
	return R

 #  miller rabin com saida true se primo ou pseudo-primo para a base e false para composto
def millerrabin(valor,base=2):
	k=0
	q=valor-1
	while q%2==0:
		k=k+1
		q/=2
	mill=expomod(base,q,valor)
	if mill==1 or mill==valor-1:
		return True
	i=1
	while i<k:

		mill=expomod(mill,2,valor)
		if mill==valor-1:
			return True
		i=i+1
	return False

#Algoritmo Euclidiano Estendido
def AEE(e,n):


        A=e
        B=n
        AUXAB=0
        X1=1
        X2=0
        AUX=0
        AUX1X2=0
        Y1=0
        Y2=1
        AUY1Y2=0
        QUO=0

        if B!=0:
            while B>0:
               QUO=A//B
               AUX=B
               B=A%B
               A=AUX

               AUX1X2=X1-QUO*X2
               X1=X2
               X2=AUX1X2

               AUY1Y2=Y1-QUO*Y2
               Y1=Y2
               Y2=AUY1Y2

               if B!=0:

                  if B==1:
                      d=X2
            return d

#Funcao que calcula o MDC entre dois numeros
def MDC(n1,n2):
	num1 = n1
	num2 = n2
	quo = 0
	resto = 0
	while(num2 != 0):
		resto = num1%num2
		quo = num1/num2
		num1 = num2
		num2 = resto
	return num1

 # funcao que calcula o phi de um determinado numero
def phiden(n):
	continua=0
	num=n
	c=0
	div=1
	auxnum=0
	auxdiv=0
	resto=0

	while(div<num and continua==0):
		auxnum=num
		auxdiv=div
		resto=1
		while(resto!=0):
			resto=auxnum%auxdiv
			if(resto==0):
				if(auxdiv==1 and div!=1):
					c=div
					continua=1
				div=div+1
			else:
				auxnum=auxdiv
				auxdiv=resto
	return c


#funcoes 1) modo de geracao de chaves--------------------------------------------------

#funcoes para salvar arquivos
def salvarchavesgamal(p,g,c,a):
    escolha = ''
    while(escolha != "e" and escolha != "s"):
        print("Digite 's' para salvar as chaves em arquivo ou 'e' para exibir as chaves no terminal.")
        escolha = raw_input()
        if(escolha == "s"):
            print("Voce escolheu salvar as chaves geradas em arquivos. Os arquivos possuem os seguintes nomes : ChavePublica e ChavePrivada.")
            print("")
            chavespublicas=open("ChavePublica", 'w')
            chavespublicas.write(p + "\n")
            chavespublicas.write(g + "\n")
            chavespublicas.write(c + "\n")
            chavesprivadas=open("ChavePrivada", 'w')
            chavesprivadas.write(a + "\n")
            chavesprivadas.write(p + "\n")
            chavesprivadas.write(g + "\n")
            print("Os arquivos ChavePublica e ChavePrivada foram salvos com sucesso!\n")
            sys.exit(0)
        elif(escolha == "e"):
            print("Voce escolheu 'exibir' as chaves no terminal.")
            print("")
            print("Chave publica:")
            print(p,g,c)
            print("Chave privada:")
            print(a)
        else:
            print("Opcao invalida, tente novamente!"+"\n")
            print("")
def salvarchaves(num,e,d):
	escolha = ''
	while(escolha != "e" and escolha != "s"):
		print("Digite 's' para salvar as chaves em arquivo ou 'e' para exibir as chaves no terminal.")
		escolha = raw_input()
        if(escolha == "s"):
            print("Voce escolheu salvar as chaves geradas em arquivos. Os arquivos possuem os seguintes nomes : ChavePublica e ChavePrivada.")
            print("")
            chavespublicasF = open("ChavePublica", 'w')
            chavespublicasF.write(num + "\n")
            chavespublicasF.write(e + "\n")
            chavesprivadasF = open("ChavePrivada", 'w')
            chavesprivadasF.write(num + "\n")
            chavesprivadasF.write(d + "\n")
            print("Os arquivos ChavePublica e ChavePrivada foram salvos com sucesso!\n")
            sys.exit(0)
        elif(escolha == "e"):
            print("Voce escolheu 'exibir' as chaves no terminal.")
            print("")
            print("Chave publica:")
            print(num,e)
            print("Chave privada:")
            print(num,d)
        else:
            print("Opcao invalida, tente novamente!"+"\n")
            print("")


 # Funcao que calcula as chaves publicas e privadas do RSA
def RSAgerador():
    p=int(geradordeprimo(128)) #gerar primo p

    q=int(geradordeprimo(128)) #gerar primo q

    num=p*q

    phi=(p-1)*(q-1)

    e=2
    MDC(phi,e)
    while MDC(phi,e)!=1:
        e=e+1

    d=AEE(e,phi)
    while d<0:
        d=phi+d

    e=decparahex(e)
    num=decparahex(num)
    d=decparahex(d)

    while(len(e)<64):
        e="0"+e
	while(len(num)<64):
		num="0"+num
    while(len(d)<64):
        d="0"+d

	print("""Chaves geradas!""")

    salvarchaves(num,e,d)

 #funcao que gera chaves de criptografia El Gamal
def GAMALgerador():
	q=10
	p=10
	g=2
	a=0
	c=0
	print("Aguarde um instante, o programa esta gerando as chaves...\n")
	while(millerrabin(q,2) != True or millerrabin(p,2) != True or q.bit_length() != 255 or p.bit_length() != 256):
		q=random.getrandbits(255)
		p=q*2+1
	while(expomod(g,q,p)==1):
		g=g+1
	a = random.randint(2,p-2)
	c = expomod(g,a,p)

	print("Chaves geradas!")
	p=decparahex(p)
	g=decparahex(g)
	c=decparahex(c)
	a=decparahex(a)
	while(len(p)<64):
		p="0"+p
	while(len(g)<64):
		g="0"+g
	while(len(c)<64):
		c="0"+c
	while(len(a)<64):
		a="0"+a

	salvarchavesgamal(p,g,c,a)


 #funcao secundaria modo  par de chaves de criptografia
def chavescriptografia():
	escolha=9
	while(escolha!=1 and escolha!=2 and escolha!=3 and escolha!=0):
		print("""
		Opcao 1 - Para o metodo de Criptografia El Gamal
		Opcao 2 - Para o metodo de Criptografia RSA
		Opcao 3 - Voltar ao MENU principal
		Opcao 0 - SAIR do programa
		----------------------""")
		while (escolha!=1 and escolha!=2 and escolha!=3 and escolha!=0):
			print("Digite a opcao desejada:")
			escolha=int(input())
			if escolha==1:
				print("Opcao 1 - Metodo de Criptografia El Gamal,escolhida.")
				GAMALgerador()
			elif escolha==2:
				print("Opcao 2 - Metodo de Criptografia RSA, escolhida.")
				RSAgerador()
			elif escolha==0:
				#sair do programa
				print("""Opcao 0 - SAIR do programa, escolhida.""")
			elif escolha==3:
				#voltar ao menu principal
				print("""Opcao 3 - Voltar ao MENU PRINCIPAL, escolhida.""")
				menuprincipal()


# funcao pricipal do (1) - modo geracao de chaves
def geradordechaves():
	escolha=9
	while(escolha!=1 and escolha!=2 and escolha!=3 and escolha!=0):

		print("""
		Opcao 1: Para criar um par de chaves de assinatura
		Opcao 2: Para criar um par de chaves de criptografia
		Opcao 3: Para voltar ao MENU PRINCIPAL
		Opcao 0: SAIR do programa
		---------------------""")
		print("Digite a opcao desejada:")
		escolha=int(input())
		if(escolha==1):
			print("""Opcao 1 - Par de chaves de assinatura, escolhida.
			""")
			GAMALgerador()
		elif(escolha==2):
			print("""Opcao 2 - Par de chaves de Criptografia, escolhida.
			""")
			chavescriptografia()
		elif(escolha==3):
			print("""Opcao 3 - Voltar ao MENU PRINCIPAL, escolhida.
			""")
			menuprincipal()
		elif(escolha==0):
			print("""Opcao 0 - Sair do programa,escolhida.
			""")
			return 1
		else:
			print("""Opcao invalida, tente novamente!
				""")
#funcoes 2)Modo de encriptacao(pura)--------------------------------------------
def RSAencriptacao(arquivo): #colocar no menuprincipal
    escolha=9
    nomearquivo=''
    existearquivo=False
    arquivochave=''
    while(escolha!=1 and escolha!=2 and escolha!=3 and escolha!=0):
        print("""
        Opcao 1 - Para digitar a chave publica em hexadecimal atraves do teclado
        Opcao 2 - Para ler a chave publica em hexadecimal atraves de um arquivo
        Opcao 3 - Voltar ao MENU PRINCIPAL
        Opcao 0 - SAIR do programa
        ---------------------
        """)
        print("Escolha a opcao desejada:")
        escolha=int(input())
        if escolha==1:
            print("Opcao 1 - Para digitar a chave publica em hexadecimal atraves do teclado,escolhida.")
            print("Digite as chaves publicas 'n' e 'e' respectivamente:")
            num=raw_input()
            e=raw_input()
        elif escolha==2:
            print("Opcao 2 - Para ler a chave publica em hexadecimal atraves de um arquivo,escolhida.")
            while existearquivo==False:
                print("Digite o nome do arquivo que contem a Chave publica:")
                nomearquivo=raw_input()
                if(os.path.exists(nomearquivo)):
                    print("Arquivo selecionado!\n")
                    existearquivo=True
                    arquivochave=open(nomearquivo,'r')
                    num=arquivochave.readline()
                    e=arquivochave.readline()
                    num=num[:-1]
                    e=e[:-1]
                else:
                    print("Arquivo nao encontrado,tente novamente!")
        elif escolha==3:
            print("Opcao 3 - Voltar ao MENU PRINCIPAL,escolhida.")
            menuprincipal()
        elif escolha==0:
            print("Opcao 0 - SAIR do programa,escolhida")
        else:
            print("Arquivo nao encontrado,tente novamente!")

        arquivoinicial = open(arquivo,'r')
    	leitura = arquivoinicial.read()
    	caracter = 0
    	print("Digite o nome do novo arquivo encriptado com RSA:")
    	encriptado=raw_input()
    	arquivonovo=open(encriptado, 'w')
    	blocos = ''

    	print("Aguarde um momento o arquivo esta sendo encriptado...")
    	while(caracter<len(leitura)):
    		blocos=(ord(leitura[caracter])+100)
    		blocos=expomod(blocos, int(hexparadec(e)), int(hexparadec(num)))
    		arquivonovo.write(str(blocos)+"\n")
    		caracter=caracter+1

        print("Encriptacao concluida!")
        sys.exit(0)






def ElGencriptacao(arquivo):
    escolha=9
    nomearquivo=''
    existearquivo=False
    arquivochave=''
    while(escolha!=1 and escolha!=2 and escolha!=3 and escolha!=0):
        print("""
        Opcao 1 - Para digitar a chave publica em hexadecimal atraves do teclado
        Opcao 2 - Para ler a chave publica em hexadecimal atraves de um arquivo
        Opcao 3 - Voltar ao MENU PRINCIPAL
        Opcao 0 - SAIR do programa
        ---------------------
        """)
        print("Escolha a opcao desejada:")
        escolha=int(input())
        if escolha==1:
            print("Opcao 1 - Para digitar a chave publica em hexadecimal atraves do teclado,escolhida.")
            print("Digite as chaves publicas 'p','g' e 'c' respectivamente:")
            p=raw_input()
            g=raw_input()
            c=raw_input()
        elif escolha==2:
            print("Opcao 2 - Para ler a chave publica em hexadecimal atraves de um arquivo,escolhida.")
            while existearquivo==False:
                print("Digite o nome do arquivo que contem a Chave publica:")
                nomearquivo=raw_input()
                if(os.path.exists(nomearquivo)):
                    print("Arquivo selecionado!")
                    existearquivo=True
                    arquivochave=open(nomearquivo,'r')
                    p=arquivochave.readline()
                    g=arquivochave.readline()
                    c=arquivochave.readline()
                    p=p[:-1]
                    g=g[:-1]
                    c=c[:-1]
                else:
                    print("Arquivo nao encontrado,tente novamente!\n")
        elif escolha==3:
            print("Opcao 3 - Voltar ao MENU PRINCIPAL,escolhida.")
            menuprincipal()
        elif escolha==0:
            print("Opcao 0 - SAIR do programa,escolhida.")
            return 1
        else:
            print("Arquivo nao encontrado,tente novamente!\n")

        arquivoinicial = open(arquivo,'r')
    	leitura = arquivoinicial.read()
    	caracter = 0
    	print("Digite o nome do novo arquivo encriptado com El Gamal:")
    	encriptado=raw_input()
    	arquivonovo=open(encriptado, 'w')
    	blocos = ''

    	print("Aguarde um momento o arquivo esta sendo encriptado...")
        p=int(hexparadec(p))
        g=int(hexparadec(g))
        c=int(hexparadec(c))
    	while(caracter<len(leitura)):
            blocos=(ord(leitura[caracter])+100)
            k=random.randint(2,p-2)
            s=expomod(g,k,p)
            t=(blocos*expomod(c,k,p))%p
            arquivonovo.write(str(s)+"\n")
            arquivonovo.write(str(t)+"\n")
            caracter=caracter+1

        print("Encriptacao concluida!")
        sys.exit(0)

#funcao principal do modo de encriptacao pura
def encriptacaopura():
    escolha=9
    nomearquivo=''
    existearquivo=False
    print("""
    Opcao 1 - A encriptacao sera realizada com RSA
    Opcao 2 - A encriptacao sera realizada com El Gamal
    Opcao 3 - Voltar ao MENU PRINCIPAL
    Opcao 0 - SAIR do programa
    ---------------------
    """)

    while(escolha!=1 and escolha!=2 and escolha!=3 and escolha!=0):
        print("Digite a opcao escolhida:")
        escolha=int(input())
        if escolha==1:
            print("Opcao 1 - A encriptacao sera realizada com RSA,escolhida.")
            print("")

        elif escolha==2:
            print("Opcao 2 - A encriptacao sera realizada com El Gamal,escolhida")
            print("")

        elif escolha==3:
            print("Opcao 3 - Voltar ao MENU PRINCIPAL,escolhida.")
            menuprincipal()
        elif escolha==0:
            print("Opcao 0 - SAIR do programa,escolhida")
            sys.exit(0)
    while(existearquivo==False):

        print("Digite o nome do arquivo que sera encriptado:")
        nomearquivo=raw_input()
        if (os.path.exists(nomearquivo)):
            print("Arquivo selecionado!")
            existearquivo=True
            if escolha==1:
                RSAencriptacao(nomearquivo)
            elif escolha==2:
                ElGencriptacao(nomearquivo)
        else:
            print("Arquivo nao encontrado,tente novamente!\n")

#funcoes 3)Modo de decriptacao---------------------------------

def ElGdecriptacao(arquivo):
    escolha=9
    p=0
    g=0
    a=0
    print("""
    Opcao 1 - Para digitar a Chave privada em hexadecimal atraves do teclado
    Opcao 2 - Para ler a chave privada em hexadecimal atraves de um arquivo
    Opcao 3 - Voltar ao MENU PRINCIPAL
    Opcao 0 - SAIR do programa
    ----------------------
    """)
    while(escolha!=1 and escolha!=2 and escolha!=0 and escolha!=3):
        escolha=int(input())
        if escolha==1:
            print("Opcao 1 - Para digitar a Chave privada em hexadecimal atraves do teclado,escolhida.")
            print("Digite a Chave privada: 'a' privado,o primo 'p' e o gerador 'g' publicos respectivamente:")
            a=raw_input()
            p=raw_input()
            g=raw_input()
        elif escolha==2:
            print("Opcao 2 - Para ler a chave privada em hexadecimal atraves de um arquivo,escolhida.")
            existearquivo=False
            arquivochave=''
            nomearquivo=''
            while(existearquivo==False):
                print("Digite o nome do arquivo que contem a chave privada:")
                nomearquivo=raw_input()
                if(os.path.exists(nomearquivo)):
                    print("Arquivo selecionado!\n")
                    existearquivo=True
                    arquivochave=open(nomearquivo, 'r')
                    a=arquivochave.readline()
                    p=arquivochave.readline()
                    g=arquivochave.readline()
                    a=a[:-1]
                    p=p[:-1]
                    g=g[:-1]
                else:
                    print("Arquivo nao encontrado, tente novamente!\n")
        elif escolha==3:
            menuprincipal()
        elif escolha==0:
            print("Opcao 0 - SAIR do programa,escolhida")
            sys.exit(0)
        else:
            print("Opcao invalida, tente novamente!")
    a=int(hexparadec(a))
    p=int(hexparadec(p))
    g=int(hexparadec(g))
    arquivoinicial=open(arquivo,'r')
    print("Digite o nome do novo arquivo desencriptografado com El Gamal:")
    leitura=raw_input()
    arquivonovo=open(leitura,'w')
    sblocos=arquivoinicial.readline()
    tblocos=arquivoinicial.readline()
    print("")
    print("Aguarde um momento, o arquivo esta sendo desencriptografado...")
    while(sblocos!=''):
        temporario = expomod(int(sblocos),(p-1-a),p)
        blocos = ((temporario*int(tblocos))%p)
        blocos = chr((int(blocos)-100))
        arquivonovo.write(blocos)
        sblocos = arquivoinicial.readline()
        tblocos = arquivoinicial.readline()
    print("Descriptografia concluida!")
    sys.exit(0)

def RSAdecriptacao(arquivo):
    escolha=9
    num=0
    d=0
    print("""
    Opcao 1 - Para digitar a Chave privada em hexadecimal atraves do teclado
    Opcao 2 - Para ler a chave privada em hexadecimal atraves de um arquivo
    Opcao 3 - Voltar ao MENU PRINCIPAL
    Opcao 0 - SAIR do programa
    ----------------------
    """)
    while(escolha!=1 and escolha!=2 and escolha!=0 and escolha!=3):
        escolha=int(input())
        if escolha==1:
            print("Opcao 1 - Para digitar a Chave privada em hexadecimal atraves do teclado,escolhida.")
            print("Digite a chave privada:'num' e 'd' respectivamente:")
            num=raw_input()
            d=raw_input()
        elif escolha==2:
            print("Opcao 2 - Para ler a chave privada em hexadecimal atraves de um arquivo,escolhida.")
            existearquivo=False
            arquivochave=''
            nomearquivo=''
            while(existearquivo==False):
                print("Digite o nome do arquivo que contem a chave privada:")
                nomearquivo=raw_input()
                if(os.path.exists(nomearquivo)):
                    print("Arquivo selecionado!")
                    existearquivo=True
                    arquivochave=open(nomearquivo, 'r')
                    num=arquivochave.readline()
                    d=arquivochave.readline()
                    num=num[:-1]
                    d=d[:-1]
                else:
                    print("Arquivo nao encontrado, tente novamente!\n")
        elif escolha==3:
            menuprincipal()
        elif escolha==0:
            print("Opcao 0 - SAIR do programa,escolhida.")
            sys.exit(0)
        else:
            print("Opcao invalida, tente novamente!\n")
    num=int(hexparadec(num))
    d=int(hexparadec(d))
    arquivoinicial=open(arquivo,'r')
    print("Digite o nome do novo arquivo descriptografado com RSA:")
    leitura=raw_input()
    arquivonovo=open(leitura,'w')
    l=arquivoinicial.readline()
    print("Aguarde um momento, o arquivo esta sendo descriptografado...")
    while(l!=''):
        blocos=l
        blocos=expomod(int(blocos),d,num)
        blocos=chr((int(blocos)-100))
        arquivonovo.write(blocos)
        l=arquivoinicial.readline()
    print("Descriptografia concluida!")
    sys.exit(0)

def decriptacaopura():
    escolha=9
    nomearquivo=''
    existearquivo=False
    print("""
    Opcao 1 - A decriptacao sera realizada com RSA
    Opcao 2 - A decriptacao sera realizada com El Gamal
    Opcao 3 - Voltar ao MENU PRINCIPAL
    Opcao 0 - SAIR do programa
    ---------------------
    """)
    while(escolha!=1 and escolha!=2 and escolha!=3 and escolha!=0):
         print("Digite a opcao escolhida:")
         escolha=int(input())
         if escolha==1:
             print("Opcao 1 - A decriptacao sera realizada com RSA,escolhida.")
             print("")
         elif escolha==2:
             print("Opcao 2 - A encriptacao sera realizada com El Gamal,escolhida.")
             print("")
         elif escolha==3:
             print("Opcao 3 - Voltar ao MENU PRINCIPAL,escolhida.")
             menuprincipal()
         elif escolha==0:
             print("Opcao 0 - SAIR do programa,escolhida")
             sys.exit(0)
    while(existearquivo==False):
        print("Digite o nome do arquivo que sera decriptado:")
        nomearquivo=raw_input()
        if (os.path.exists(nomearquivo)):
            print("Arquivo selecionado!")
            existearquivo=True
            if escolha==1:
                RSAdecriptacao(nomearquivo)
            elif escolha==2:
                ElGdecriptacao(nomearquivo)
        else:
            print("Arquivo nao encontrado,tente novamente!")
# funcao 4) modo de assinatura digital pura
def assdigital(arquivoinicial,a,p,gerador):
	nomearquivo = open(arquivoinicial, 'r')
	arquivoassina = nomearquivo.read()
	c=0
	texto = ''
	print("Aguarde um instante, o arquivo esta sendo lido...")
	while(c < len(arquivoassina)):
		blocos=(ord(arquivoassina[c]))
		converteparabinario = lambda x: format(x,'b')
		blocos=converteparabinario(blocos)
		texto=str(texto)+str(blocos)
		c=c+1
	print("Leitura concluida!\n")
	p = int(hexparadec(p))
	g = int(hexparadec(gerador))
	a = int(hexparadec(a))
	k = random.randint(2,p-2)
	while(MDC(k,p-1)!=1):
		k=random.randint(2,p-2)
	r=expomod(g,k,p)
	kmdc = AEE(k, p-1)
	h = sha224(texto).hexdigest()
	h = int(hexparadec(h))
	converteparabinario = lambda x: format(x, 'b')
	h = int(converteparabinario(h))
	s = (kmdc*(h-a*r))%(p-1)
	r = int(r)
	s = int(s)
	r = decparahex(r)
	s = decparahex(s)
	while(len(r)<64):
		r="0"+r
	while(len(s) < 64):
		s="0"+s
	print("Digite o nome do arquivo em que deseja salvar a assinatura:")
	nomeassinatura = raw_input("")
	assinatura = open(nomeassinatura, 'w')
	assinatura.write(r +"\n")
	assinatura.write(s +"\n")
	print("Arquivo assinado!\n")
	sys.exit(0)

def assinaturadigital():
	escolha=9
	arquivoassinar=''
	chavearquivo=''
	chaveprivada=''
	existearquivo=False
	existearquivo2=False
	while(existearquivo==False):
		print("Digite o nome do arquivo que deseja assinar:")
		arquivoassinar=raw_input()
		if(os.path.exists(arquivoassinar)):
			print("Arquivo selecionado!\n")
			existearquivo=True
		else:
			print("Arquivo nao encontrado,tente novamente!")
			print("")
	while(escolha!=1 and escolha!=2 and escolha!=3 and escolha!=0):
		print("""
		Opcao 1 - Para digitar a Chave privada em hexadecimal da Assinatura digital
		Opcao 2 - Para ler a Chave privada em hexadecimal da Assinatura digital de um arquivo
		Opcao 3 - Voltar ao MENU PRINCIPAL
		Opcao 0 - SAIR do programa
		----------------------
		""")
		print("Digite a opcao desejada:")
		escolha=int(input())

		if escolha==1:
			print("Opcao 1 - Para digitar a Chave privada em hexadecimal da Assinatura digital,escolhida.")
			print("Digite a chave privada 'a' e os componentes publicos 'p' e 'g' respectivamente:")
			a=raw_input()
			p=raw_input()
			g=raw_input()
		elif escolha==2:
			print("Opcao 2 - Para ler a Chave privada em hexadecimal da Assinatura digital de um arquivo,escolhida.")
			while(existearquivo2==False):
				print("Digite o nome do arquivo que contem a Chave privada:")
				chavearquivo=raw_input()
				if(os.path.exists(chavearquivo)):
					print("Arquivo localizado!"+"\n")
					existearquivo2=True
					chaveprivada=open(chavearquivo,'r')
					a=chaveprivada.readline()
					p=chaveprivada.readline()
					g=chaveprivada.readline()
					a=a[:-1]
					p=p[:-1]
					g=g[:-1]
				else:
					print("Arquivo nao encontrado,tente novamente!"+"\n")
		elif escolha==3:
			print("Opcao 3 - Voltar ao MENU PRINCIPAL")
			menuprincipal()
		elif escolha==0:
			print("Opcao 0 - SAIR do programa")
			sys.exit(0)

	assdigital(arquivoassinar,a,p,g)

#menu principal--------------------------------------------------
def menuprincipal():
	escolha=9
	while(escolha!=1 and escolha!=2 and escolha!=3 and escolha!=4 and escolha!=5 and escolha!=6 and escolha!=7):
		print("""
		----Menu principal----

		Opcao 1 - Modo de geracao de chaves
		Opcao 2 - Modo de encriptacao
		Opcao 3 - Modo de decriptacao
		Opcao 4 - Modo de assinatura digital (pura)
		Opcao 5 - Modo de verificacao de assinatura (pura)
		Opcao 6 - Modo de assinatura digital e encriptacao (combinados)
		Opcao 7 - Modo de decritacao e verificacao de assinatura (combinados)
		Opcao 0 - SAIR do programa
		----------------------
		""")
		print("Digite a opcao desejada:") #escolha do menu principal
		escolha=int(input())
		if escolha == 1:
			print("Opcao 1 - Modo de geracao de chaves escolhida.")
			geradordechaves()
		elif escolha == 2:
			print("""Opcao 2 - Modo de encriptacao escolhida.
			""")
			encriptacaopura()
		elif escolha == 3:
			print("""Opcao 3 - Modo de decriptacao escolhida.
			""")
			decriptacaopura()
		elif escolha == 4:
			print("""Opcao 4- Modo de assinatura digital(pura), escolhida.""")
			assinaturadigital()
		elif escolha == 5:
			print("""Opcao 5 - Modo de verificacao de assinatura(pura), escolhida.
			""")
		elif escolha == 6:
			print("""Opcao 6 - Modo de assinatura digital e encriptacao(combinados), escolhida.
			""")
		elif escolha == 7:
			print("""Opcao 7 - Modo de decritacao e verificacao de assinatura(combinados), escolhida.
			""")
		elif escolha ==0:
			print("""Opcao 0 - SAIR do programa, escolhida.
			""")
			sys.exit(0)
		else:
			print("Opcao invalida, tente novamente!\n")

#fim do menu principal
menuprincipal()
