#classe xcom metodos publico protegido e privado
class Pessoa:
    def __init__(self,nome,idade,email):
        self.__nome =nome #nome como public publico
        self.__idade =idade# protected protegido na palavra idade adiciona andescore no i de idade
        self.__email =email #private coloca duas andescore no inicio do atributo que neste caso o email
        
#metodo para proteger os dados 
#metodo get nome forma correta 
    @property
    def nome(self):
        return self.__nome
    #metodo set nome
    @nome.setter
    def nome(self,nome):
        self.__nome = nome
    
    @property
    def idade(self):
        return self.__idade
    #metodo set
    @idade.setter
    def idade(self,idade):
        self.__idade = idade

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,email):
        self.__email = email    


#para ter acesso aos atributos usar essas coisas mas  não e o metodo indicado
    #metodos de acesso 
    # def get_nome(self):
    #     return self.__nome


    # def set_nome(self,nome):
    #     self.__nome = nome

    # def get_idade(self):
    #     return self.__idade

    # def set_idade(self,idade):
    #     self.__idade = idade  


    # def get_email(self):
    #     return self.__email

    # def set_email(self,email):
    #     self.__email = email             