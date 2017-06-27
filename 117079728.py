'''
UFRJ - Universidade Federal do Rio de Janeiro
Disciplina: Numeros inteiros e criptografia
Professor: Menasche
Nome: David Melo da Silva
DRE: 117079728
VeRSAgeradoro:0.1 (ATUALIZADA EM :26/06/2017)

26/06/2017 - menuprincipal criado
26/06/2017 - Modo de geracao de chaves

O programa elaborado para este trabalho devera ser capaz de encriptar e/ou assinar digitalmente
qualquer arquivo salvo no computador.
1-Em caso de realizacao de uma assinatura digital,o metodo utilizado sera o El Gamal.
2-Em caso de realizacao de criptografia o metodo utilizado sera entre RSAgerador ou El Gamal
de acordo com a escolha do usuario.

'''
import os.path
import random

# Manipulacao de Arquivos
def salvarchaves(num,e,d):
	escolha = ''
	while(escolha != "e" and escolha != "s"):
		print("Digite 's' para salvar as chaves em arquivo ou 'e' para exibir as chaves no terminal")
		escolha = raw_input()

		if(escolha == "s"):
			print("Voce escolheu salvar as chaves geradas em arquivos. Os arquivos possuem os seguintes nomes : ChavePublica e ChavePrivada")
			print("")

			chavespublicasF = open("ChavePublica", 'w')
			chavespublicasF.write(num + "\n")
			chavespublicasF.write(e + "\n")
			chavesprivadasF = open("ChavePrivada", 'w')
			chavesprivadasF.write(num + "\n")
			chavesprivadasF.write(d + "\n")

			print("Os arquivos ChavePublica e ChavePrivada foram salvos com sucesso!")

		elif(escolha == "e"):
			print("Voce escolheu 'exibir' as chaves no terminal.")
			print("")
			print("Chave publica:")
			print(num,e)
			print("Chave privada:")
			print(num,d)

		else:
			print("Escolha invalida, tente novamente!")
			print("")
#---------------------------------------Fim arquivos--------------------------------------------
#funcoes

def decparahex(dec): #funcao que converte decimal para inteiro

    x = (dec % 16)
    digits = "0123456789ABCDEF"
    rest = dec / 16
    if (rest == 0):
        return digits[x]
    return decparahex(rest) + digits[x]

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
		k+=1
		q/=2
	mill=expomod(base,q,valor)
	if mill==1 or mill==valor-1:
		return True
	i=1
	while i<k:
		mill=pow(mill,2)%valor
		if mill==valor-1:
			return True
		i=i+1
	return False

def AEE(e,n): #aqui vamos calcular o d do RSAgerador


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


def MDC(n1,n2): #Funcao que calcula o MDC entre dois numeros
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

def RSAgerador(): # Funcao que calcula as chaves publicas e privadas do RSAgerador
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

	print("Chaves geradas com sucesso!")
	print("")
    salvarchaves(num,e,d)



#menu principal
def menuprincipal(escolha):

    if escolha == 1:
        print("Opcao 1 - Modo de geracao de chaves escolhido.")
        print("""
        Opcao 1: para criar um par de chaves de assinatura
        Opcao 2: para criar um par de chaves de criptografia
        ----------------------
        """)

        print("Digite a opcao desejada:") #escolha do menu "geracao de chave escolhido"
        escolha=int(input()) #escolha digitada pelo usuario


        if escolha == 1:
            print("Opcao 1 - Par de chaves de assinatura escolhido.")

        elif escolha == 2:
            print("Opcao 2 - Par de chaves de criptografia escolhido.")
            print("""
            Opcao 1 - Para o metodo de Criptografia El Gamal
            Opcao 2 - Para o metodo de Criptografia RSA
            ----------------------
            """)

            print("Digite a opcao desejada:")
            escolha=int(input()) #escolha digitada pelo usuario

            if escolha == 1:
                print("Opcao 1 - Metodo El Gamal escolhido.")
                print(" ")

            elif escolha == 2:
                print("Opcao 2 - Metodo RSA escolhido.")
                print(" ")

                RSAgerador()

            else:
    			print("Escolha invalida, tente novamente!")
    			return 1
        else:
            print("Escolha invalida, tente novamente!")
            return 1




    elif escolha == 2:
        print("Opcao 2 - Modo de encriptacao escolhido.")
    elif escolha == 3:
        print("Opcao 3 - Modo de decriptacao escolhido.")
    elif escolha == 4:
        print("Opcao 4- Modo de assinatura digital(pura) escolhido.")
    elif escolha == 5:
        print("Opcao 5 - Modo de verificacao de assinatura(pura) escolhido.")
    elif escolha == 6:
        print("Opcao 6 - Modo de assinatura digital e encriptacao(combinados) escolhido.")
    elif escolha == 7:
        print("Opcao 7 - Modo de decritacao e verificacao de assinatura(combinados) escolhido.")
    else:
        print("Escolha invalida, tente novamente!")


#fim ddo menu principal

# programa principal
print("""
----Menu principal----

Opcao 1 - Modo de geracao de chaves
Opcao 2 - Modo de encriptacao
Opcao 3 - Modo de decriptcao
Opcao 4 - Modo de assinatura digital (pura)
Opcao 5 - Modo de verificacao de assinatura (pura)
Opcao 6 - Modo de assinatura digital e encriptacao (combinados)
Opcao 7 - Modo de decritacao e verificacao de assinatura (combinados)
----------------------
""")

print("Digite a opcao desejada:") #escolha do menu principal
escolha=int(input()) #escolha digitada pelo usuario
menuprincipal(escolha) #funcao menuprincipal

#fim do programa principal
