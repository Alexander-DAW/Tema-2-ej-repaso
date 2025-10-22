class Empleado:
    _lista_dni = set()
    salario_medio = []
    def __init__(self, nombre , salario, dni):
        self.__nombre=nombre
        self.__salario=salario
        self.__dni=dni
        if dni in Empleado._lista_dni:
            raise ValueError(f"El DNI {dni} ya está en uso.")
        Empleado._lista_dni.add(dni)

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def salario(self):
        return self.__salario
    
    @property
    def dni(self):
        return self.__dni
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    def detalles(self):
        print(f'''Nombre: {self.get_nombre()},
              Salario: {self.get_salario()}.
              DNI: {self.get_dni()}''')
        
    def __del__(self):
        print(f"Objeto con DNI {self.dni} destruido.")

    @classmethod
    def calcular_salario_medio(cls):
        print(f"Salario medio: {cls.salario_medio}")

class Gerente:
    def __init__(self, nombre , salario, dni, departamento):
        super().__init__(nombre , salario, dni)
        self.__departamento = departamento
    
    @property
    def departamento(self):
        return self.__departamento
    
    @departamento.setter
    def departamento(self, departamento):
        self.__departamento = departamento

    def descuento_sueldo (self):
        return self.salario - self.salario * 0.1
    
    @staticmethod
    def impuesto(salario):
        return salario * 1.21
    
    def detalles(self):
        print (super().detalles() + (f"Departamento: {self.departamento}"))



    
    



