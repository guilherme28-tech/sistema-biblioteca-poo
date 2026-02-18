class Livro():
    """   
    Representa um livro dentro da biblioteca.

    Atributos:
        id (int): Identificador único do livro.
        titulo (str): Título do livro.
        autor (str): Autor do livro.
        disponivel (bool): Indica se o livro está disponível para empréstimo.
    """
    def __init__(self, id, titulo, autor, disponivel=True):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

    def __str__(self):
        if self.disponivel == True:
            status = "Disponivel."
        else:
            status = "Emprestado."
        return f"{self.id} - {self.titulo} - {self.autor} ({status})"