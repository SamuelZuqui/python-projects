# CALCULADORA PYTHON SAMUEL !!!

def boas_vindas(): # DEFININDO FUNÇÃO BOAS VINDAS
    print("\n Seja bem vindo à calculadora do Samuel!")

def calculadora(): # DEFININDO FUNÇÃO CALCULADORA
    escolha = input('''
Escolha a opção desejada: \n
1 -> Soma
2 -> Subtração
3 -> Multiplicação
4 -> Divisão
5 -> Potência \n
''')
    
    if escolha == '1':
        print("VOCÊ ESCOLHEU SOMAR! ENTÃO:")
        n1 = int(input("\n Digite o primeiro número: "))
        n2 = int(input("\n Digite o segundo número: "))
        print(' {} + {} = ' .format(n1, n2))
        print(n1 + n2)

    elif escolha == '2':
        print("VOCÊ ESCOLHEU SUBTRAIR! ENTÃO:")
        n1 = int(input("\n Digite o primeiro número: "))
        n2 = int(input("\n Digite o segundo número: "))
        print(' {} - {} = ' .format(n1, n2))
        print(n1 - n2)

    elif escolha == '3':
        print("VOCÊ ESCOLHEU MULTIPLICAR! ENTÃO:")
        n1 = int(input("\n Digite o primeiro número: "))
        n2 = int(input("\n Digite o segundo número: "))
        print(' {} * {} = ' .format(n1, n2))
        print(n1 * n2)

    elif escolha == '4':
        print("VOCÊ ESCOLHEU DIVIDIR! ENTÃO:")
        n1 = int(input("\n Digite o primeiro número: "))
        n2 = int(input("\n Digite o segundo número: "))
        if n2 == 0:
            print("\n Não é possível dividir por 0")
        else:
            print(' {} / {} = ' .format(n1, n2))
            print(n1 / n2)

    elif escolha == '5':
        print("VOCÊ DECIDIU CALCULAR A POTÊNCIA ENTÃO:")
        n1 = int(input("\n Digite o primeiro número: "))
        n2 = int(input("\n Digite o segundo número: "))
        print(' {} ** {} = ' .format(n1, n2))
        print(n1 ** n2)

    else:
        print("\n Opção inválida")
        

    retorno()


def retorno():
    retornar_calc = input('''
Você deseja usar a calculadora novamente? \n
Se SIM, digite "S", se NÃO, digite "N"
''')
    
    if retornar_calc.upper() == 'S':
        calculadora()

    elif retornar_calc.upper() == 'N':
        print ("Obrigado por usar a calculadora!")
    else:
        retorno()


# INÍCIO DO PROGRAMA
boas_vindas()
calculadora()




