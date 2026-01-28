class Autor():
    def __init__(self, nome):
        self.nome = nome
 
class Livro():
    def __init__(self, titulo, nome_autor):
        self.titulo = titulo
        self.autor = Autor(nome_autor).nome
    
    def __str__(self):
        return f"Livro - {self.titulo}\nAutor - {self.autor}"

livro = Livro("Arsenalta", "Vinicius")
print(livro.__str__())