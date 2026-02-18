from projeto_biblioteca.livro import Livro
from projeto_biblioteca.usuario import Usuario


class Biblioteca():
    """
        Classe responsável por gerenciar o sistema da biblioteca.

    Atributos:
        livros (list): Lista de objetos Livro cadastrados.
        usuarios (list): Lista de objetos Usuario cadastrados.
        ids_livros (int): Contador automático para IDs de livros.
        ids_usuarios (int): Contador automático para IDs de usuários.

    Métodos:
        adicionar_livro: Cadastra um novo livro.
        cadastrar_usuario: Cadastra um novo usuário.
        emprestar_livro: Realiza o empréstimo de um livro.
        devolver_livro: Registra a devolução de um livro.
        listar_livros: Exibe todos os livros cadastrados.
        listar_usuarios: Exibe todos os usuários cadastrados.
    """
    def __init__(self):
        self.livros = []
        self.ids_livros = 1
        self.usuarios = []
        self.ids_usuarios = 1

# >>>>>>>>>>>>

#   CADASTRO

# <<<<<<<<<<<<

    def adicionar_livro(self, titulo, autor):
        livro = Livro(self.ids_livros, titulo, autor)
        self.livros.append(livro)
        self.ids_livros += 1
        print(f"O livro {titulo}, de {autor}, foi adicionado à biblioteca com sucesso!")
        return None


    def cadastrar_usuario(self, nome): 
        usuario = Usuario(self.ids_usuarios, nome)
        self.usuarios.append(usuario)
        self.ids_usuarios +=1
        print(f"O usuário {usuario.nome.title()}, id número {usuario.id} foi cadastrado com sucesso!")
        return None
    
# >>>>>>>>>>>

#   BUSCA

# <<<<<<<<<<<

    def buscar_livro_por_id(self, id):
        for livro in self.livros:
            if livro.id == id:
                return livro
        return None
    

    def buscar_usuario_por_id(self, id): 
        for usuario in self.usuarios:
            if usuario.id == id:
                return usuario
        return None

# >>>>>>>>>>>>>>>>>

#   EMPRÉSTIMO

# <<<<<<<<<<<<<<<<<
       
    def emprestar_livro(self, usuario_id, livro_id):
        usuario = self.buscar_usuario_por_id(usuario_id)
        livro = self.buscar_livro_por_id(livro_id)
        
        if usuario is None:
            print("Usuário não encontrado.")

        elif livro is None:
            print("O livro não foi encontrado.")

        elif livro.disponivel == False:
            print("Este livro já foi emprestado.")
            print('')
        else:
            livro.disponivel = False
            usuario.livros_emprestados.append(livro)
            print("Livro emprestado com sucesso!")

# <<<<<<<<<<<<<

#   DEVOLUÇÃO

# >>>>>>>>>>>>>

    def devolver_livro(self, usuario_id, livro_id):
        usuario = self.buscar_usuario_por_id(usuario_id)
        livro = self.buscar_livro_por_id(livro_id)
        
        if usuario is None or livro is None:
            print("Usuário ou livro não encontrado.")
            return
        if livro not in usuario.livros_emprestados:
            print("Esse usuário não possui esse livro.")
            return
        else:
            livro.disponivel = True
            usuario.livros_emprestados.remove(livro)

        print("Livro devolvido com sucesso.")

# <<<<<<<<<<<<<<<<<<<

#   LISTAGEM

# >>>>>>>>>>>>>>>>>>>

    def listar_livros(self):
        print("==== LISTA DE LIVROS ====")
        for livro in self.livros:
            if livro.disponivel == True:
                status = "Disponivel."
            else:
                status = "Emprestado."
            print(f"{livro.id} - {livro.titulo} ({status})")
        return None

    def listar_usuarios(self):
        print("==== LISTA DE USUÁRIOS ====")
        for usuario in self.usuarios:
            print(f"{usuario.id} - {usuario.nome}")
        return None