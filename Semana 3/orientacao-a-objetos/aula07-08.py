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