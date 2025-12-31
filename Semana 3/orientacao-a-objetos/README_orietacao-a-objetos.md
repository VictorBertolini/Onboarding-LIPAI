# Semana 3 - Códigos

### Nome: Victor Bertolini de Sousa

### Github: 

## Código das videoaulas

### Aula 1 – Introdução à Orientação a Objetos
```python
""" Introdução à Orientação a Objetos em Python - Parte 1 """

# paradigma de programação 

# calcular a área e o perímetro de um retangulo
# estrutura para armazenar os valores necessários para os cálculos
# area = base * altura
# perímetro = 2 * (base + altura)

retangulo1 = {
    'base':  10.0,
    'altura':  5.0
}

retangulo2 = {
    'base':  6.0,
    'altura':  3.0
}

# Realizar os cálculos
def calcular_area(retangulo):
    return retangulo['base'] * retangulo['altura']

def calcular_perimetro(retangulo):
    return 2 * (retangulo['base'] + retangulo['altura'])

print(calcular_area(retangulo1))
print(calcular_area(retangulo2))
print(calcular_perimetro(retangulo1))
print(calcular_perimetro(retangulo2))


# Classe representa um conceito
# Classe representa um retângulo
# Classe possui atributos: base e altura
# Classe possui métodos (função dentro da classe)
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

# Instanciando objetos do tipo retangulo
# Chamando método construtor
retangulo1 = Retangulo(10.0, 5.0)
retangulo2 = Retangulo(6.0, 3.0)

print(type(retangulo1), retangulo1)
print(type(retangulo2), retangulo2)

print(
    retangulo1.base,
    retangulo1.altura,
    retangulo1.calcular_area(),
    retangulo1.calcular_perimetro()
)
print(
    retangulo2.base,
    retangulo2.altura,
    retangulo2.calcular_area(),
    retangulo2.calcular_perimetro()
)
```

### Aula 2 - Atributos de instância e de classe
```python
""" Aula 02 - Atributos de classe e instância """

# Classe pessoa possui
# Atributos de instância: nome e email
# Atributos de classe: especie
class Pessoa:
    especie = 'Humano'

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

pessoa1 = Pessoa('Maria da Silva', 'maria@email.com')
pessoa2 = Pessoa('João Santos', 'joao@email.com')

# alterar um atributo de classe na instância (objeto)
# altera somente para aquela instância
pessoa1.especie = 'Alienigena'

# alterando um atributo de classe na classe
# altera todos os objetos e na classetambém
Pessoa.especie = 'Alienigenas do Passado'

print(pessoa1.nome, pessoa1.email, pessoa1.especie)
print(pessoa2.nome, pessoa2.email, pessoa2.especie)

print(Pessoa.especie)
```

### Aula 3 - Métodos de classe
```python
""" Aula 03 - Métodos de classe """

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    @classmethod
    def from_list(cls, lista):
        return cls(lista[0], lista[1])
     
    @classmethod
    def from_string(cls, rep_retangulo):
        base, altura = rep_retangulo.split(sep=',')
        return cls(float(base), float(altura))

    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

retangulo1 = Retangulo(10.0, 5.0)
retangulo2 = Retangulo(6.0, 3.0)
retangulo3 = Retangulo.from_list([20.0, 3.5])
retangulo4 = Retangulo.from_string("55.4,13.5")

print(retangulo3.base, retangulo3.altura, retangulo3.calcular_area())
print(retangulo4.base, retangulo4.altura, retangulo4.calcular_area())
```

### Aula 4 - Propriedades
```python
""" Aula 04 - Propriedades """

# forma de controlar acesso aos atributos de uma instância
# formas personalizadas de obter e alterar o valor de um atributo

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    # getter
    @property
    def base(self):
        return self._base
    
    # setter
    @base.setter
    def base(self, value):
        if value <= 0:
            raise ValueError('A base deve ser maior que zero')
        self._base = value

    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, value):
        if value <= 0:
            raise ValueError('A altura deve ser maior que zero')
        self._altura = value

    @classmethod
    def from_list(cls, lista):
        return cls(lista[0], lista[1])
    
    @classmethod
    def from_string(cls, rep_retangulo):
        base, altura = rep_retangulo.split(sep=',')
        return cls(float(base), float(altura))

    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    

retangulo1 = Retangulo(3.0, 3.0)

retangulo1.base = 3.0
retangulo1.altura = 3.0
print(retangulo1.base)
```

### Aula 5 - Métodos especiais
```python
""" Aula 05 - Métodos especiais """
# __str__(self)
# __repr__(self)

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
    # __str__(self)
    # Representação do objeto como string para humanos
    def __str__(self):
        return f'Retângulo[base={self.base}, altura é={self.altura}]'
    
    # __repr__(self)
    # Representação do objeto como string para recriar 
    # esse objeto
    # loggin, debug
    # Representação canônica
    def __repr__(self):
        return f'Retangulo({self.base},{self.altura})'

    
retangulo1 = Retangulo(10.0, 5.0)
retangulo2 = Retangulo(3.0, 14.0)

representacao_string_retangulo = 'Retangulo(7.5, 12.3)'
print(retangulo1.__repr__())

retangulo3 = eval('Retangulo(7.5, 12.3)')
retangulo4 = eval(repr(retangulo3))

print(retangulo1)
print(retangulo2)
print(retangulo3)
print(retangulo4)
```

### Aula 6 - `__eq__` e `__hash__`
```python
""" Aula 06 - Equals e HashCode """

nome1 = 'João'
nome2 = 'João'

print(nome1==nome2)

class Pessoa:
    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome
        
    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.cpf == value.cpf
        return False
    
    def __hash__(self):
        return hash(self.cpf)
    
    def __repr__(self):
        return f'Pessoa(cpf={self.cpf},{self.nome})'

pessoa1 = Pessoa('100100100-10', 'João')
pessoa2 = Pessoa('100100100-10', 'João')
pessoa3 = Pessoa('100100100-11', 'Maria')

pessoas = {pessoa1, pessoa2, pessoa3}
print(pessoas)
print(pessoa1 == pessoa2)

pessoas_lista = [pessoa1, pessoa2, pessoa3]
print(pessoas_lista)
print(pessoas_lista.count(pessoa1))
```

### Aula 7 - Relacionamento entre classes
```python
""" Aula 07 - Relacionamentos entre classes """

class Endereco:
    def __init__(self, cep, numero):
        self.cep = cep
        self.numero = numero

    def __str__(self):
        return f'Endereco[cep={self.cep}, numero={self.numero}]'

class Telefone:
    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero

    def __str__(self):
        return f'Telefone[ddd={self.ddd}, numero={self.numero}]'
        

class Pessoa:
    def __init__(self, cpf, nome, telefone, endereco):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.enderecos = [endereco]

    def add_endereco(self, endereco):
        self.enderecos.append(endereco)

    def print_enderecos(self):
        print(self.nome)
        for endereco in self.enderecos:
            print(endereco)

    def __str__(self):
        return f'Pessoa[cpf={self.cpf}, nome={self.nome}, telefone={self.telefone}, enderecos={self.enderecos}]'
    
telefone = Telefone('11', '1111-1111')
pessoa1 = Pessoa('11233213', 'João da Silva', telefone, Endereco('02233039', 123))
pessoa1.add_endereco(Endereco('92332323', 55))

pessoa2 = Pessoa('223232', 'Maria da Silva', telefone, Endereco('1231221', 33))

pessoa3 = Pessoa('3333333', 'Pedro da Silva', telefone, Endereco('1231221', 33))

print(pessoa1)
print(pessoa1.cpf, pessoa1.nome, pessoa1.telefone)
print(pessoa1.telefone.ddd, pessoa1.telefone.numero)
print(pessoa2)

pessoa1.print_enderecos()
pessoa2.print_enderecos()
pessoa3.print_enderecos()
```

### Aula 8 - Herança entre Classes – super()
```python
""" Aula 08 - Herança """

class Pessoa: 
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
    
    def obtem_nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    

class Cliente(Pessoa): 
    def __init__(self, nome, sobrenome, cpf):
        super().__init__(nome, sobrenome, cpf)
        self.compras = []


class Funcionario(Pessoa): 
    def __init__(self, nome, sobrenome, cpf, salario):
        super().__init__(nome, sobrenome, cpf)
        self.salario = salario

    def calcula_pagamento(self):
        return self.salario - ((10/100) * self.salario)


class Programador(Funcionario): 
    def __init__(self, nome, sobrenome, cpf, salario, bonus):
        super().__init__(nome, sobrenome, cpf, salario)
        self.bonus = bonus

    def calcula_pagamento(self):
        pagamento_salario = super().calcula_pagamento()
        return pagamento_salario + self.bonus


programador = Programador("Jose", "Augusto", "123.123.123-12", 5000, 200)
print(programador.obtem_nome_completo())
print(programador.calcula_pagamento())
print(type(programador))


# funcionario = Funcionario("Jose", "Augusto", "123.123.123-12", 5000)
# print(funcionario.obtem_nome_completo())
# print(funcionario.calcula_pagamento())
# print(type(funcionario))


# cliente = Cliente("Paulo", "Mulloto", "123.123.123-12")
# print(cliente.obtem_nome_completo())
# print(type(cliente))
```

## Exercícios 

### Exercício 1 
```python
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
```

### Exercício 2
```python
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
```

### Exercício 3 
```python
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
```

### Exercício 4 
```python
""" Exercício 4 - Orientação a Objetos

Lista de participações no Projeto
○ Altere a classe Projeto para:
■ Incluir um atributo do tipo list chamado participacoes.
■ Essa lista deve armazenar objetos da classe Participacao.
○ Implemente também o método:
def add_participacao(self, participacao):
Adiciona uma participação ao projeto.
...
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
        self.participacoes = [] 

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

    def add_participacao(self, participacao):
        self.participacoes.append(participacao)


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

aluno = Aluno.from_string("SP0101,João da Silva,joao.silva@usp.br")
projeto = Projeto.from_string("1,Desenvolvimento de Software,Prof. Silva")

participacao = Participacao(
    codigo="P001",
    data_inicio="2025-03-01",
    data_fim="2025-12-31",
    aluno=aluno,
    projeto=projeto
)

projeto.add_participacao(participacao)

print(len(projeto.participacoes))  
print(projeto.participacoes[0].aluno.nome)  
```









