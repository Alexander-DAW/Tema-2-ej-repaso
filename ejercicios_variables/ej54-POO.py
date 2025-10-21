class Empleado:
    salario_medio = []
    def __init__(self, nombre , salario, dni):
        self.__nombre=nombre
        self.__salario=salario
        self.__dni=dni

    def get_nombre(self):
        return self.__nombre
    
    def get_salario(self):
        return self.__salario
    
    def get_dni(self):
        return self.__dni
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_salario(self, salario):
        self.__salario = salario

    def set_dni(self, dni):
        self.__dni = dni

    def detalles(self):
        print(f'''Nombre: {self.get_nombre()},
              Salario: {self.get_salario()}.
              DNI: {self.get_dni()}''')
    
    @classmethod
    def calcular_salario_medio(cls):
        print(f"Salario medio: {cls.salario_medio  }")



