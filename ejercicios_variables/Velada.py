class FueraDeRango(Exception):
    pass

class PersonaDuplicada(Exception):
    def __init__(self, nombre_persona):
        super().__init__(f"{nombre_persona} ya aparece en nuestra base de datos. Prueba otra persona. ")
    pass

class Evento:
    
    entradas_vendidas = 0
    
    def __init__(self, evento):
        self.__evento = evento
        self.tipos_entrada = {"general": 25.0,
                         "premium": 60.0,
                         "vip": 120.0
                         }
        self.__combates = {}
        self.__artistas = {}
        self.__entradas = {}
        self.__staff = {}

    @property
    def evento(self):
        return self.__evento
    
    @evento.setter
    def evento(self, evento):
        self.__evento = evento
    
    @property
    def combates(self):
        return self.__combates
    
    @combates.setter
    def combates(self, combates):
        self.__combates = combates

    @property
    def artistas(self):
        return self.__artistas
    
    @artistas.setter
    def artistas(self, artistas):
        self.__artistas = artistas

    @property
    def entradas(self):
        return self.__entradas
    
    @entradas.setter
    def entradas(self, entradas):
        self.__entradas = entradas

    @property
    def staff(self):
        return self.__staff
    
    @staff.setter
    def staff(self, staff):
        self.__staff = staff

    def montar_reservas(self):
        self.combastes=[self.combates]
        self.artistas=[self.artistas]
        self.entradas=[self.entradas]
        self.staff=[self.staff]



    def vender_entradas(self, tipo, unidades):
        costo_entrada = 0
        for nombre_tipo, precio in self.tipos_entrada.items():
            if nombre_tipo == tipo:
                costo_entrada = precio * unidades
        self.entradas["vendidas"] = self.entradas_vendidas
        self.entradas["tipos"] = self.tipos_entrada
        print(self.entradas)
        print(f"Tipo de entrada: {tipo}\nUnidades: {unidades}\n- Se han vendido {unidades} entradas {tipo} por un total de {costo_entrada} euros")

    def agregar_artista(self, nombre, setlist):
        print(f"Nombre del artista: {nombre}\n ")


    


class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

class Luchador(Persona):
    def __init__(self, nombre, peso):
        super().__init__(nombre)
        self.__peso = peso
    
    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.__peso = peso
        

class Artista(Persona):
    def __init__(self, nombre, *temas):
        super().__init__(nombre)
        self.__temas = temas
    
    @property
    def temas(self):
        return self.__temas

    @temas.setter
    def temas(self, temas):
        self.__temas = temas


class Combate:
    def __init__(self, titulo, peso, rounds):
        pass

class Entrada:

    def __init__(self, tipo, unidades):
        self.__tipo = tipo
        self.__unidades = unidades
        Evento.entradas_vendidas+=unidades

    @property
    def tipo(self):
        return self.__tipo
        
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def unidades(self):
        return self.__unidades
        
    @unidades.setter
    def unidades(self, unidades):
        self.__unidades = unidades
    


Velada = Evento({})

def Menu():
    print(f"Bienvenido al Backstage Manager de la Velada de Ibai.\nElige una de las siguientes funciones:\n{'-' * 30}\n1. Vender entradas\n2. Añadir artista\n3. Programar combates\n4. Cerrar combate\n5. Ver informe completo del evento\n6. Salir")
    while True:
        try:
            user = int(input("Selecciona una opción: "))
            if 1 <= user <= 6:
                print(f"Opcion {user} elegida.")       
                match user:
                    case 1:
                        while True:
                            try:
                                tipo_entrada=int(input(f"Que tipo de entrada quiere: \n1. General\n2. Premium\n3. Vip\n "))
                                unidades = int(input("Cuantas entradas desea comprar: "))
                                if 1 <= tipo_entrada <= 3:
                                    match tipo_entrada:
                                        case 1:
                                            tipo_entrada = "general"
                                        case 2:
                                            tipo_entrada = "premium"
                                        case 3:
                                            tipo_entrada = "vip"
                                    entrada = Entrada(tipo_entrada, unidades)
                                    Velada.vender_entradas(entrada.tipo, entrada.unidades)
                                    break
                                else:
                                    raise FueraDeRango("Opción fuera de rango. Elige un número entre 1 y 3.")
                            except ValueError:
                                print("Respuesta invalida. Debe ingresar un numero entero.")
                            except FueraDeRango as e_u:
                                print(e_u)
                    case 2:
                        while True:
                            try:
                                nombre_artista = str(input("Introduzca el nombre del artista: ")).strip().lower().capitalize()
                                temas_artista = input("Introduce las canciones separadas por comas: ").strip()
                                setlist_artista = [cancion.strip() for cancion in temas_artista.split(",")]
                                set_setlist = set(setlist_artista)
                                artista = Artista(nombre_artista, set_setlist)
                                Velada.agre
                            except ValueError:
                                print("Respuesta invalida. Pruebe de nuevo")

                            

            else:
                raise FueraDeRango("Opción fuera de rango. Elige un número entre 1 y 6.")
        except ValueError:
            print("Respuesta invalida. Debes ingresar un número entero")
        except FueraDeRango as e:
            print(e)


Menu()