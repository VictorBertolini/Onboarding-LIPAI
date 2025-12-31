""" Exercício 2 - Orientação a Objetos 

Classe Projeto
○ Implemente uma classe Projeto com:
■ Atributos:
● codigo – número inteiro que representa o código do
projeto
● titulo
● responsavel – nome do professor responsável pelo
projeto
■ Requisitos:
● Deve ser possível construir um objeto projeto a partir de
uma string no formato: "codigo,titulo,responsavel"
Exemplo: "1,Laboratório de Desenvolvimento de
Software,Pedro Gomes"
● Nenhum dos atributos pode ser vazio ou nulo (use
propriedades).
● O atributo codigo deve ser armazenado como inteiro.
● Dois projetos devem ser considerados iguais se tiverem
o mesmo código (codigo).
● Implemente __eq__ comparando pelo código.

"""

class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel

    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, value):
        if not value:
            raise ValueError("Código não pode ser vazio ou nulo.")
        self._codigo = int(value)

    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, value):
        if not value:
            raise ValueError("Título não pode ser vazio ou nulo.")
        self._titulo = value

    @property
    def responsavel(self):
        return self._responsavel
    
    @responsavel.setter
    def responsavel(self, value):
        if not value:
            raise ValueError("Responsável não pode ser vazio ou nulo.")
        self._responsavel = value

    @classmethod
    def from_string(cls, rep_projeto):
        codigo, titulo, responsavel = rep_projeto.split(sep=',')
        return cls(int(codigo), titulo, responsavel)
    
    def __eq__(self, other):
        if isinstance(other, Projeto):
            return self.codigo == other.codigo
        return False
    

projeto1 = Projeto.from_string("1,Laboratório de Desenvolvimento de Software,Pedro Gomes")
projeto2 = Projeto.from_string("1,Laboratório de Desenvolvimento de Software,Pedro Gomes")
print(projeto1 == projeto2)  

print(projeto1.codigo)
print(projeto1.titulo)
print(projeto1.responsavel)