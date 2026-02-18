class Usuario():
    """
    Representa um usuário da biblioteca.

    Atributos:
        id (int): Identificador único do usuário.
        nome (str): Nome do usuário.
        livros_emprestados (list): Lista de livros atualmente emprestados pra esse usuário.
    """
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.livros_emprestados = []
    
    def __str__(self):
        return f"{self.id} - {self.nome}"
        