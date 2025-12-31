""" Exercício 1 - Orientação a Objetos 

Classe Aluno
○ Implemente uma classe Aluno com:
■ Atributos:
● prontuario
● nome
● email
■ Requisitos:
● Deve ser possível construir um objeto Aluno a partir de
uma string no formato: "prontuario,nome,email"
Exemplo: "SP0101,João da Silva, joao@email.com"
● Nenhum dos atributos pode ser vazio ou nulo.
● Use propriedades (@property e setters) para validar os
valores.
● Dois alunos devem ser considerados iguais se tiverem o
mesmo prontuário.
● Implemente o método especial __eq__ para comparar
objetos Aluno por prontuário.
● (Opcional, mas recomendado) Considere também
implementar __hash__ se quiser usar alunos em
conjuntos (set) ou como chaves de dicionário.
"""

class Aluno:
    def __init__(self, prontuario, nome, email):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email

    @property
    def prontuario(self):
        return self._prontuario
    
    @prontuario.setter
    def prontuario(self, value):
        if not value:
            raise ValueError("Prontuário não pode ser vazio ou nulo.")
        self._prontuario = value

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, value):
        if not value:
            raise ValueError("Nome não pode ser vazio ou nulo.")
        self._nome = value

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if not value:
            raise ValueError("Email não pode ser vazio ou nulo.")
        self._email = value

    @classmethod
    def from_string(cls, aluno_str):
        prontuario, nome, email = aluno_str.split(',')
        return cls(prontuario.strip(), nome.strip(), email.strip())

    def __eq__(self, other):
        if isinstance(other, Aluno):
            return self.prontuario == other.prontuario
        return False

    def __hash__(self):
        return hash(self.prontuario)

aluno1 = Aluno.from_string("SP0101,João da Silva,joao@email.com")

print(aluno1.prontuario)
print(aluno1.nome)
print(aluno1.email)

aluno2 = Aluno.from_string("SP0101,Maria Souza,maria@email.com")
print(aluno1 == aluno2)  

