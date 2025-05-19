def menu():
    opcoes = int(input("Digite a opção desejada(1-Adicionar arquivo; 2-Sair):  "))
    if opcoes == 1:
        inserirArquivo()
    elif opcoes == 2:
       fecharPrograma()


def inserirArquivo():
    adicionarNome = input("adiciona um nome aí: ")
    with open("adicionarArquivo.txt", "a") as insereArquivo:
        insereArquivo.write(adicionarNome)
    novaAtividade = input("deseja realizar mais alguma ação?(s/n): ")
    if novaAtividade == "s":
        menu()
    else:
        print("encerrando arquivo")
def fecharPrograma():

    print("encerrando arquivo")

menu()