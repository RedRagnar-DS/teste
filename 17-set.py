filmesSet = {"Uma Batalha após a outra","MIB","Pecadores","Godzilla","Naruto","Jujutsu Kaisen","Agente Secreto"}
print(type(filmesSet))
#1 - Retornar o tamanho do Set
print(len(filmesSet))
#2 - O true e o 1 são considerados o mesmo valor
exemploSet = {"Teste hoje",True,1, 8.7}
print(exemploSet)
#3 - Adicionar outro set

filmesSet.update(exemploSet)
print(filmesSet)
#4 - Removendo elementos do Set
filmesSet.remove(True)
filmesSet.remove(8.7)
print(filmesSet)
