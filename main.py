class User():
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self._password = password
        
    def authenticate_password(self, password):
        return self._password == password
    
    def change_password(self, new_password):
        self._password = new_password
    
class Aluno(User):
    def __init__(self, name, email, password, matricula, data_entrada, data_saida, cpf) -> None:
        self.matricula = matricula
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.__cpf = cpf
        super().__init__(name, email, password)
    
    def get_cpf(self):
        return self.__cpf

class Professor(User):
    def __init__(self, name, email, password, matricula, salario, materia):
        self.matricula = matricula
        self.__salario = salario
        self.materia = materia
        super().__init__(name, email, password)

    def get_salario(self):
        return self.__salario
