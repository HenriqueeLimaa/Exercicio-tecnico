from Application import Application

app = Application()


def program():

    print("Bem vindo ao programa para consulta de bolsas.")
    print("Digite o número para consultar a opção desejada:")
    print("1- Consultar bolsa zero/ano: ")
    print("2- Codificar nome: ")
    print("3- Consultar media anual: ")
    print("4- Consultar ranking de valores de bolsa: ")
    print("0- Encerrar o programa.\n")

    user_choice = input("Digite o número de sua consulta: ")

    if user_choice == '1':
        app.search_one()
    elif user_choice == '2':
        app.search_two()
    elif user_choice == '3':
        app.search_three()
    elif user_choice == '4':
        app.search_four()
    elif user_choice == '0':
        print('Programa encerrado!')
        return
    else:
        print("\n Entrada invalida, tente novamente.\n")
        program()


program()