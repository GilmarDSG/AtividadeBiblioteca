

livros = []


def adicionar_livro(titulo, autor):
    livro = {"titulo": titulo, "autor": autor}
    livros.append(livro)
    print(f"Livro '{titulo}' adicionado com sucesso!")


def remover_livro(titulo):
    for livro in livros:
        if livro["titulo"].lower() == titulo.lower():
            livros.remove(livro)
            print(f"Livro '{titulo}' removido com sucesso!")
            return
    print(f"⚠ Livro '{titulo}' não encontrado.")


def listar_livros():
    if not livros:
        print("📚 Nenhum livro cadastrado.")
    else:
        print("\n--- Lista de Livros ---")
        for i, livro in enumerate(livros, start=1):
            print(f"{i}. {livro['titulo']} - {livro['autor']}")


def buscar_livro(titulo):  # 🔹 veja que está no singular
    for livro in livros:
        if titulo.lower() in livro["titulo"].lower():
            print(f"Livro encontrado: {livro['titulo']} - {livro['autor']}")
            return
    print(f"Nenhum livro encontrado com o título '{titulo}'.")
