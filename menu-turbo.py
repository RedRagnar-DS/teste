import os

dicionariofilmes={}
p=""
i=0 

class Filme:
    def adicionar(self,nome,lancamento,genero):
        return{
            "nome":nome,
            "lancamento":lancamento,
            "genero":genero 
        }
        

gerenciador = Filme()        
#Dt=gerenciador.adicionar("As branquelas",2001,["comedia","besteirol"])
#dicionariofilmes[0]=Dt
#print(dicionariofilmes)

while p!="fim":
    os.system('cls')
    print("               ==Locadora==")
    print("Adicionar filmes")
    n=input("Nome do filme:  ")
    l=input("Data de lançamento:  ")
    g=input("Genero:  ")

    temp=[n, l, g]

    nome, lancamento, genero= temp

    dt=gerenciador.adicionar(nome,lancamento,genero)
    dicionariofilmes[i] = dt
    i += 1
    p = input("Digite 'fim' para parar ou Enter para continuar: ").lower()

    print(dicionariofilmes)








