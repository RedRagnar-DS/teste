#Tuplas
filmestuplas = ("Uma Batalha após a outra","MIB","Pecadores","Godzilla","Naruto","Jujutsu Kaisen","Agente Secreto")
print(filmestuplas)
print(type(filmestuplas))
#Buscar os dois primeiros elementos da tupla
print(filmestuplas[:2])
#Buscar o ultimo item
print(filmestuplas[-1])
#Buscar filmes de uma determinada posição
print(filmestuplas[1:1+3])
#Buscar filmes de uma posição em diante
print(filmestuplas[4:])
#resgatando o idice da tupla pelo nome
print(filmestuplas.index("MIB"))
print(filmestuplas.index("Naruto"))