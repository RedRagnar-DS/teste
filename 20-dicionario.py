filme={
    "Titulo": "MIB",
    "Lancamento": 2000,
    "Rating": 9.5,
    "Genero": ["Ficção","Suspense","Trilogia"]
}
print(filme)
print(len(filme))
print(type(filme))

#1 - Recuperar um elemento do dicionário

print(filme["Genero"])
print(filme.get("Rating"))

#2 - Buscar apenas as chaves dp dicionário
print(filme.keys())
#3 - Buscar apenas os valores do dicionário
print(filme.values())
#4 - Buscar itens do dicionário com chave e valor
print(filme.items())
#5 - Adicionar um item no dicionário
filme["Diretor"]="Christopher Nolan"
print(filme)
#6 - Atualizar um valor
filme.update({"Rating":10.0})
print(filme)
#7 - Remover item
filme.pop("Diretor")
print(filme)