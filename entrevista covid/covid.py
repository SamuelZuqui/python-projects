
# BOAS VINDAS AO USUÁRIO
print ("Olá! Seja bem vindo(a) à pesquisa para avaliar se você faz parte do grupo de risco do COVID-19")

# RECOMENDAÇÃO:
# Por favor, vamos evitar contato físico, não dividir copos e talheres, manter o ambiente arejado e higienizar sempre as mãos, superfícies e objetos.


# SEQUÊNCIA DE PERGUNTAS:
sexo = input('Qual é o seu gênero? Masculino("M"), Feminino("F"), Outros não especificados anteriormente("O") ou Prefere não responder("X")?') 
if sexo.upper() == "F" or sexo == "O" or sexo == "X": # Usando .upper() para aceitar minúsculas
    gravida = input("Ok, você está gravida? Sim ('S') ou Não ('N')")
    if sexo.upper() == "F" and gravida.upper() == "S": 
        print("Você é do grupo de risco do COVID-19!")
    else: 
        idade = int(input("Qual é a sua idade?"))
        if idade >= 60:
            print("Você é do grupo de risco do COVID-19!")
        else: 
            doença = input("Possui alguma comorbidade? (Asma, Diabetes, Hipertensão ou Câncer). Sim ('S') ou Não ('N')? ")
            if doença.upper() == "S":
                print("Você é do grupo de risco do COVID-19!")
            else:
                print("Oba, você não faz parte do grupo de risco do COVID-19.")
                print("Mesmo assim, deixo aqui, minhas recomendações:")
                print("Por favor, vamos evitar contato físico, não dividir copos e talheres, manter o ambiente arejado e higienizar sempre as mãos, superfícies e objetos.")

elif sexo.upper() == "M":
    idade = int(input("Qual é a sua idade:"))
    if idade >=60:
        print("Você é do grupo de risco do COVID-19!")
    else:
        doença = input("Possui alguma cormobidade? (Asma, Diabetes, Hipertensão ou Câncer). Sim ('S') ou Não ('N')? ")
        if doença.upper() == "S":
                print("Você é do grupo de risco do COVID-19!")
        else:
            print("Oba, você não faz parte do grupo de risco do COVID-19.")
            print("Mesmo assim, deixo aqui, minhas recomendações:")
            print("Por favor, vamos evitar contato físico, não dividir copos e talheres, manter o ambiente arejado e higienizar sempre as mãos, superfícies e objetos.")










                    







