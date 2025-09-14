from livro import (
    adicionar_livro,
    remover_livro,
    listar_livros,
    buscar_livro
)

def menu():
    while True:
        print("\n--- Menu da Biblioteca ---")
        print("1. Adicionar livro")
        print("2. Remover livro")
        print("3. Listar livros")
        print("4. Buscar livro")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            adicionar_livro(titulo, autor)

        elif opcao == "2":
            titulo = input("Digite o título do livro a remover: ")
            remover_livro(titulo)

        elif opcao == "3":
            listar_livros()

        elif opcao == "4":
            titulo = input("Digite o título do livro a buscar: ")
            buscar_livro(titulo)

        elif opcao == "5":
            print("Saindo da biblioteca. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
