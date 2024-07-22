from main import *

class TestUser():
    def test_password():
        user = User(
            "Luiz", 
            "luiz@email.com", 
            "2012aa", 
        )
        
        user.change_password("201ba")
        if user.authenticate_password("201ba") == False:
            print("User: Test failed, password returned incorrect")
            return False

        print("User: Test successful")


class TestAluno():
    def test_get_cpf():
        aluno = Aluno(
            "Luiz", 
            "luiz@email.com", 
            "2012aa", 
            "2021109", 
            "04/05/2021", 
            "12/01/2025", 
            "000.000.000-00"
        )
        if aluno.get_cpf() != "000.000.000-00":
            print("Aluno: Test failed, method returned incorrect CPF")
            return False

        print("Aluno: Test successful")
        return True
        
class TestProfessor():     
    def test_get_salario():
        professor = Professor(
            "Rafael", 
            "rafael@email.com", 
            "rafael321", 
            "201390", 
            100000, 
            "Projeto de Desenvolvimento de Software"
        )

        if professor.get_salario() != 100000:
            print("Professor: Test failed, method returned incorrect salary")
            return False
        
        print("Professor: Test successful")
        return True

TestUser.test_password()
TestAluno.test_get_cpf()
TestProfessor.test_get_salario()
