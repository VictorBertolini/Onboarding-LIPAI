""" Exercício 3 - Orientação a Objetos 

Classe Participacao
○ Implemente uma classe Participacao com os seguintes atributos:
■ codigo – identificador da participação (pode ser inteiro ou
string, você escolhe, mas seja consistente)
■ data_inicio
■ data_fim
■ aluno – um objeto da classe Aluno
■ projeto – um objeto da classe Projeto associado
○ Você pode começar armazenando as datas como strings (ex:
"2025-03-01"). Em atividades futuras, podemos trabalhar com tipos de
data mais específicos.

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

class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto

    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, value):
        if not value:
            raise ValueError("Código não pode ser vazio ou nulo.")
        self._codigo = value
    
    @property
    def data_inicio(self):
        return self._data_inicio
    
    @data_inicio.setter
    def data_inicio(self, value):
        if not value:
            raise ValueError("Data de início não pode ser vazia ou nula.")
        self._data_inicio = value
    
    @property
    def data_fim(self):
        return self._data_fim
    
    @data_fim.setter
    def data_fim(self, value):
        if not value:
            raise ValueError("Data de fim não pode ser vazia ou nula.")
        self._data_fim = value
    
    @property
    def aluno(self):
        return self._aluno
    
    @aluno.setter
    def aluno(self, value):
        self._aluno = value

    @property
    def projeto(self):
        return self._projeto
    
    @projeto.setter
    def projeto(self, value):
        self._projeto = value


Participacao1 = Participacao(
    codigo="P001",
    data_inicio="2025-03-01",
    data_fim="2025-12-31",
    aluno=Aluno.from_string("SP0101,João da Silva,joao.silva@usp.br"),
    projeto=Projeto.from_string("1,Desenvolvimento de Software,Prof. Silva"))

print(Participacao1.codigo)
print(Participacao1.data_inicio)
print(Participacao1.data_fim)
print(Participacao1.aluno.nome)
print(Participacao1.projeto.titulo)

