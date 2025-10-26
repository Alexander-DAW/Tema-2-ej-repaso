liga = {
    "League of Legends": {
        "Dragons": {
            "jornada1": [8.5, 9.0, 8.7, 8.8],
            "jornada2": [9.1, 8.9, 9.2, 9.0],
            "jornada3": [9.4, 9.5, 9.3, 9.4]
        },
        "Titans": {
            "jornada1": [8.0, 8.1, 8.3, 8.2],
            "jornada2": [8.5, 8.6, 8.7, 8.6]
        }
    },
    "Valorant": {
        "Spectres": {
            "jornada1": [9.0, 9.1, 8.9, 9.2],
            "jornada2": [9.3, 9.2, 9.4, 9.5],
            "jornada3": [9.5, 9.6, 9.7, 9.6]
        },
        "Phantoms": {
            "jornada1": [8.4, 8.5, 8.3, 8.6],
            "jornada2": [8.8, 8.7, 8.9, 8.8]
        }
    },
    "Counter-Strike 2": {
        "HeadHunters": {
            "jornada1": [9.1, 9.3, 9.2, 9.1],
            "jornada2": [9.5, 9.4, 9.6, 9.5],
            "jornada3": [9.7, 9.6, 9.8, 9.7]
        },
        "Recoil Masters": {
            "jornada1": [8.8, 8.7, 8.9, 8.8],
            "jornada2": [9.0, 8.9, 9.1, 9.0]
        }
    },
    "Fortnite": {
        "SkyBuilders": {
            "jornada1": [9.2, 9.1, 9.3, 9.4],
            "jornada2": [9.6, 9.5, 9.7, 9.6]
        },
        "StormRiders": {
            "jornada1": [8.7, 8.8, 8.6, 8.9],
            "jornada2": [8.9, 9.0, 9.1, 9.0],
            "jornada3": [9.3, 9.2, 9.4, 9.3]
        }
    }
}


def calcular_media_puntuaciones(liga, **kwargs):
    """
    Calcula la media de las puntuaciones y mostrar datos de forma organizada

    Parametros:
        -liga (dict): Diccionario con los equipos, sus jornadas y sus puntuaciones
        -kwargs
            -equipo (str, opcional): Nombre del juego al que vamos a cambiarle las puntuaciones
            -jornada (str, opcional): Nombre de la jornada a actualizar
            -puntuaciones (list, opcional): Lista de puntuasciones adicionales para agregar a la fase
            
    Return:
        - dic: Diccionario con los equipos y su media de puntuacion total
    """

    resultado = {}

    equipo_nombre = kwargs.get("equipo")
    jornada_nombre = kwargs.get("jornada")
    puntuaciones_adicionales = kwargs.get("puntuacion")

    print(f"\nResultados de la liga\n")

    for juego, equipos in liga.items():
        print(f"Juego: {juego.upper()}\n{'-' * (11+len(juego))}")

        for equipo, jornadas in equipos.items():
            if equipo_nombre.lower() == equipo.lower():
                if jornada_nombre in jornadas:
                    jornadas[jornada_nombre].extend(puntuaciones_adicionales)
                else:
                    jornadas[jornadas] = puntuaciones_adicionales
            print(f"\nEquipo : {equipo}")
            medias_por_jornada = []

            for jornada, puntuaciones in jornadas.items():
                puntuaciones_redondeadas = list(map(lambda puntuacion: round(puntuacion, 2), puntuaciones))
                media_jornada = sum(puntuaciones_redondeadas) / len (puntuaciones_redondeadas)
                medias_por_jornada.append(media_jornada)
                print(f" - {jornada}: Media = {round(media_jornada, 2)}\n")
            
            media_total = sum(medias_por_jornada) / len(medias_por_jornada)
            resultado[equipo] = round(media_total, 2)

            print(f"\nMEDIA TOTAL : {round(media_total)}") 
        print("\n" + "=" * 50 + "\n")
    print(resultado) 

            

            

print(calcular_media_puntuaciones(liga, equipo="Valorant"))