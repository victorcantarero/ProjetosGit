def salvar_contatos(lista):
    arquivo = open("contatos.txt", "w")

    for contato in lista:
        arquivo.write("nome:{}/email:{}/telefone:{}/twitter:{}/instagram:{}/facebook:{}\n ".format(contato['nome'],
                                                                                                   contato['telefone'],
                                                                                                   contato['email'],
                                                                                                   contato['twitter'],
                                                                                                   contato['instagram'],
                                                                                                   contato['facebook']))
    arquivo.close()



def existe_contato(lista, email):  # o email vai ser ultilizado para identificação dos contatos, pois cada email dos
    # contatos são únicos
    if len(lista) > 0:
        for contato in lista:
            if contato['email'] == email:
                return True
    return False


def adicionar(lista):  # função de cadastro na agenda
    while True:
        email = input("Digite o e-mail do contato: ")

        if not existe_contato(lista, email):
            break
        else:
            print("Esse e-mail já foi ultilizado.")
            print("Por favor, tente um novo e-mail. ")

    contato = {
        "email": email,
        "nome": input("Digite o seu Nome:"),
        "telefone": input("Digite o seu Telefone:"),
        "twitter": input("Digite o seu nick no Twitter:"),
        "instagram": input("Digite o seu nick no Instagram:"),
        "facebook": input("Digite o seu nick no Facebook:"),
    }

    lista.append(contato)
    print("o contato {} foi cadastrado com sucesso!\n".format(contato['nome']))


def listar(lista):  # essa função vai mostrar os contatos na agenda
    print("===================Listar contatos=======================")
    if len(lista) > 0:
        print("o contato foi encontrado. As informações seguem abaixo: ")
        for i, contato in enumerate(lista):
            print("contato {}:".format(i + 1))
            print("\tNome: {}".format(contato['nome']))
            print("\tEmail: {}".format(contato['email']))
            print("\tTelefone: {}".format(contato['telefone']))
            print("\tTwitter: {}".format(contato['twitter']))
            print("\tInstagram: {}".format(contato['instagram']))
            print("\tFacebook: {}".format(contato['facebook']))
            print("========================================================\n")
        print("Quantidade de contatos: {}\n".format(len(lista)))
    else:
        print("Não existe nenhum contato cadastrado no sistema.\n")
        return


def deletar(lista):  # essa função vai deletar os contatos na agenda
    print("===================Excluir contato=======================")
    if len(lista) > 0:
        email = input("Digite o e-mail do contato a ser excluído: ")
        if existe_contato(lista, email):
            print("o contato foi encontrado. As informações seguem abaixo: ")
            for i, contato in enumerate(lista):
                if contato['email'] == email:
                    print("Nome: {}".format(contato['nome']))
                    print("Email: {}".format(contato['email']))
                    print("Telefone: {}".format(contato['telefone']))
                    print("Twitter: {}".format(contato['twitter']))
                    print("Instagram: {}".format(contato['instagram']))
                    print("Facebook: {}".format(contato['facebook']))
                    print("========================================================\n")

                del lista[i]

                print("O contato foi apagado com sucesso!")
                break

        else:
            print("Não existe contato cadastrado no sistema com o email informado {}.\n".format(email))

    else:
        print("Não existe nenhum contato cadastrado no sistema.\n")
        return


def buscar(lista):  # essa função vai buscar os contatos na agenda
    print("===================Buscar contato=======================")
    if len(lista) > 0:
        email = input("Digite o contato do e-mail a ser encontrado: ")
        if existe_contato(lista, email):
            print("o contato foi encontrado. As informações seguem abaixo: ")
            for contato in lista:
                if contato['email'] == email:
                    print("Nome: {}".format(contato['nome']))
                    print("Email: {}".format(contato['email']))
                    print("Telefone: {}".format(contato['telefone']))
                    print("Twitter: {}".format(contato['twitter']))
                    print("Instagram: {}".format(contato['instagram']))
                    print("Facebook: {}".format(contato['facebook']))
                    print("========================================================\n")
                    break
        else:
            print("Não existe contato cadastrado no sistema com o email informado {}.\n".format(email))

    else:
        print("Não existe nenhum contato cadastrado no sistema.\n")


def alterar(lista):
    print("===================Alterar contato=======================")
    if len(lista) > 0:
        email = input("Digite o contato do e-mail que vai ser alterado: ")
        if existe_contato(lista, email):
            print("o contato foi encontrado. As informações seguem abaixo: ")
            for contato in lista:
                if contato['email'] == email:
                    print("Nome: {}".format(contato['nome']))
                    print("Email: {}".format(contato['email']))
                    print("Telefone: {}".format(contato['telefone']))
                    print("Twitter: {}".format(contato['twitter']))
                    print("Instagram: {}".format(contato['instagram']))
                    print("Facebook: {}".format(contato['facebook']))
                    print("========================================================\n")

                contato['nome'] = input("digite o novo nome do contato: ")
                contato['telefone'] = input("digite o novo telefone do contato: ")
                contato['twitter'] = input("digite o novo twitter do contato: ")
                contato['instagram'] = input("digite o novo instagram do contato: ")
                contato['facebook'] = input("digite o novo facebook do contato: ")
                print("Os dados do contato com o email {}, foram alterados com sucesso!".format(contato['email']))
                break
        else:
            print("Não existe contato cadastrado no sistema com o email informado {}.\n".format(email))

    else:
        print("Não existe nenhum contato cadastrado no sistema.\n")


def principal():  # função para o menu principal da agenda

    lista = []

    while True:
        print("===================Agenda Pessoal=======================")
        print("[1]Cadastrar contato")
        print("[2]listar contato")
        print("[3]Deletar contato")
        print("[4]Buscar contato")
        print("[5]Alterar informações de um contato já cadastrado")
        print("[6]Sair")
        print("========================================================")
        print("Escolha uma opcao Acima:")
        opcao = int(input("> "))

        if opcao == 1:
            adicionar(lista)
            salvar_contatos(lista)
        elif opcao == 2:
            listar(lista)
        elif opcao == 3:
            deletar(lista)
            salvar_contatos(lista)
        elif opcao == 4:
            buscar(lista)
        elif opcao == 5:
            alterar(lista)
            salvar_contatos(lista)
        elif opcao == 6:
            print("Saindo do programa...")
            break
        else:
            print("opcao invalida. Por favor, tente novamente.")


principal()
