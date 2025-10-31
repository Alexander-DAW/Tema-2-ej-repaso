class FueraDeRango(Exception):
    pass

class TituloDuplicado(Exception):
    pass

class PersonaDuplicada(Exception):
    def __init__(self, nombre_persona):
        super().__init__(f"{nombre_persona} ya aparece en nuestra base de datos. Prueba otra persona. ")
    pass

class Evento:
    
    tipos_entrada = {"general": 25.0,
                         "premium": 60.0,
                         "vip": 120.0
                         }

    def __init__(self, evento):
        self.__evento = {}
        self.__combates = {}
        self.__artistas = []
        self.__entradas = {}
        self.__staff = {}
        self.entradas_vendidas = 0

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
        self.evento["combates"] = self.combates
        self.evento["artistas"] = self.artistas
        self.evento["entradas"] = self.entradas

        
    def vender_entradas(self, tipo, unidades):
        costo_entrada = 0
        for nombre_tipo, precio in self.tipos_entrada.items():
            if nombre_tipo == tipo:
                costo_entrada = precio * unidades
        self.entradas["vendidas"] = self.entradas_vendidas
        self.entradas["tipos"] = self.tipos_entrada
        print(self.entradas)
        print(f"Tipo de entrada: {tipo}\nUnidades: {unidades}\n- Se han vendido {unidades} entradas {tipo} por un total de {costo_entrada} euros")

    def agregar_artista(self, nombre, *setlist):
        print(f"Nombre del artista: {nombre}\n. Artista añadido correctamente")
        artista_dic = {
            "nombre" : nombre,
            "setlist" : list(setlist)
        }
        self.artistas.append(artista_dic)
        print(self.artistas)

    def programar_combate(self, titulo, luchadores, rounds, peso):
        datos_combate = {
            "luchadores" : luchadores,
            "rounds": rounds,
            "peso": peso,
            "resultado" : None
        }
        self.combates[titulo] = datos_combate

    def informe_completo(self):
        self.montar_reservas()
        print ("Informe de la velada")
        for i in self.evento:
            print(f"Numero de combates: {len(combates)}")

        
    


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
    def __init__(self, nombre):
        super().__init__(nombre)
    
        

class Artista(Persona):
    def __init__(self, nombre, temas):
        super().__init__(nombre)
        self.__temas = temas
    
    @property
    def temas(self):
        return self.__temas

    @temas.setter
    def temas(self, temas):
        self.__temas = temas


class Combate:
    def __init__(self, titulo, peso, rounds, luchadores):
        self.__titulo = titulo
        self.__peso = peso
        self.__rounds = rounds
        self.__luchadores = luchadores
    
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.titulo = titulo

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.peso = peso

    @property
    def rounds(self):
        return self.__rounds

    @rounds.setter
    def rounds(self, rounds):
        self.rounds = rounds

    @property
    def luchadores(self):
        return self.__luchadores

    @luchadores.setter
    def luchadores(self, luchadores):
        self.luchadores = luchadores


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
    


Velada = Evento()

def menu():
    print(f"Bienvenido al Backstage Manager de la Velada de Ibai.\nElige una de las siguientes funciones:\n{'-' * 30}")
    while True:
        try:
            user = int(input("1. Vender entradas\n2. Añadir artista\n3. Programar combates\n4. Cerrar combate\n5. Ver informe completo del evento\n6. Salir\nSelecciona una opción del menu: "))
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
                                if artista.nombre in Velada.artistas:
                                    raise PersonaDuplicada(nombre_artista)
                                else:
                                    Velada.agregar_artista(artista.nombre, artista.temas)
                                    break
                            except ValueError:
                                print("Respuesta invalida. Pruebe de nuevo")
                            except PersonaDuplicada as epd:
                                print (epd)
                    case 3:
                        while True:
                            try:
                                lista_luchadores = []
                                titulo_combate = str(input("Introduza el titulo de combate: ")).strip().lower().capitalize()
                                rounds = int(input("Introduce el numero de rondas: "))
                                peso = str(input("Introduce el peso la pelea ")).strip().lower()
                                try:
                                    if titulo_combate not in Velada.combates.keys():
                                        for luchador in range(2):
                                            try:
                                                luchador_nombre= str(input(f"Introduce el nombre del luchador {luchador + 1} : ")).strip().lower().capitalize()
                                                if luchador_nombre not in lista_luchadores:
                                                    luchador = Luchador(luchador_nombre)
                                                    lista_luchadores.append(luchador.nombre)
                                                else:
                                                    raise PersonaDuplicada (luchador_nombre)
                                            except ValueError:
                                                print("Respuesta invalida. Pruebe de nuevo")
                                            except PersonaDuplicada as e_u:
                                                print(e_u)
                                        combate = Combate(titulo_combate, lista_luchadores, rounds, peso )
                                        Velada.programar_combate(combate.titulo, combate.luchadores, combate.rounds, combate.peso)
                                    else:
                                        raise TituloDuplicado("Este titulo ya existe.")                    
                                    break
                                except TituloDuplicado as aeo:
                                    print(aeo)
                            except ValueError:
                                print("Respuesta invalida. Pruebe de nuevo")                                    

                                
                                    
                                        

                                        

        
            else:
                raise FueraDeRango("Opción fuera de rango. Elige un número entre 1 y 6.")
        except ValueError:
            print("Respuesta invalida. Debes ingresar un número entero")
        except FueraDeRango as e:
            print(e)


if __name__ == "__main__":    
    menu()