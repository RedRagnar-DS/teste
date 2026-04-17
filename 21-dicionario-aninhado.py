import pprint

filmesGeral = {
        "MIB":{
    "Lancamento": 2000,
    "Rating": 9.5,
    "Genero": ["Ficção","Suspense","Trilogia"]
    },
    "GATTACA":{
    "Lancamento": 1990,
    "Rating": 10.0,
    "Genero": ["Ficção","Suspense",""]
    },
    "A Vida é Bela":{
    "Lancamento": 2019,
    "Rating": 9.0,
    "Genero": ["Drama","Guerra","Crítica"]
    },
    "Os Inscriveis":{
    "Lancamento": 2000,
    "Rating": 9.5,
    "Genero": ["Animação","Familia","Ficção"]
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmesGeral)
print(len(filmesGeral))

#1 Buscar uma informação dentro de um dicionario aninhado

print(filmesGeral["GATTACA"]["Lancamento"])

#2 - Adicionar novo["[ item
filmesGeral["MIB"]["Diretor"] = "Stieve Sphilberg"
#pp.pprint(filmesGeral)
print(filmesGeral)

#Excluir um dicionario

del filmesGeral["MIB"]

pp.pprint(filmesGeral)