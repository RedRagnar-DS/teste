import subprocess as spr
import time

while True:
    spr.run("cls",shell=True)#Limpa a tela
    print("="*22)
    print("*** Menu Principal ***\n")
    print("="*22)
    print("\n1 - Area Triangulo")
    print("2 - Todos Calculos")
    print("3 - Par ou Impar")
    print("4 - Comparação de Números")
    print("5 - Fases da Vida")
    print("6 - Contator")
    print("7 - Repetição usando For")
    print("8 - Tabuada de um numero")
    print("9 - Lista")
    print("10 - String")
    print("11 - Lista Palavras")
    print("12 - Exercicios")
    print("13 - Fazendo Calculos")
    print("14 - Criar Lista")
    print("15 - Analise de Temperatura")
    print("16 - Metodo de Lista")
    print("17 - Set")
    print("18 - Tupla")
    print("19 - Triangulo Turbo pro Max")
    print("20 - Dicionário")
    print("21 - Dicionário Aninhado")
    print("0 - Sair do Programa")

    opcao = input("Escolha: ")

    if opcao == "1":
        spr.run(["python", "1-area_triangulo.py"])
    elif opcao == "2":
        spr.run(["python", "2-todos_calculos.py"])
    elif opcao == "3":
        spr.run(["python", "3-par_impar.py"])
    elif opcao == "4":
        spr.run(["python", "4-compara_numeros.py"])
    elif opcao == "5":
        spr.run(["python", "5-fase_vida.py"])
    elif opcao == "6":
        spr.run(["python", "6-contador.py"])
    elif opcao == "7":
        spr.run(["python", "7-repeticao_for2.py"])
    elif opcao == "8":
        spr.run(["python", "8-tabuada_de_um_numero.py"])
    elif opcao == "9":
        spr.run(["python", "9-lista.py"])
    elif opcao == "10":
        spr.run(["python", "10-string.py"])
    elif opcao == "11":
        spr.run(["python", "11-lista_palavras.py"])
    elif opcao == "12":
        spr.run(["python", "12-exercicio.py"])
    elif opcao == "13":
        spr.run(["python", "13-fazendo_calculos.py"])
    elif opcao == "14":
        spr.run(["python", "14-criar_lista.py"])
    elif opcao == "15":
        spr.run(["python", "15-analise_temperatura.py"])
    elif opcao == "16":
        spr.run(["python", "16-metodo_lista.py"])
    elif opcao == "17":
        spr.run(["python", "17-set.py"])
    elif opcao == "18":
        spr.run(["python", "18-tupla.py"])
    elif opcao == "19":
        spr.run(["python", "19-triangulo2.py"])
    elif opcao == "20":
        spr.run(["python", "20-dicionario.py"])
    elif opcao == "21":
        spr.run(["python", "21-dicionario-aninhado.py"])
    elif opcao == "0":
        break
    else:
        print("\n[*** opção invalida ***]")
    time.sleep(10)

   # match(opcao):
   #     case "1":
   #         spr.run(["python", "tabuada_turbo.py"])
    #    case "2":
    #        spr.run(["python", "9-lista.py"])