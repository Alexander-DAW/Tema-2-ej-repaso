grupos = {
    "chirigotas": {
        "Los Yesterday": {
            "preliminares": [9.1, 9.3, 9.0, 9.2],
            "cuartos": [9.4, 9.2, 9.1, 9.3],
            "semifinal": [9.6, 9.5, 9.4, 9.5],
            "final": [9.7, 9.6, 9.8, 9.7]
        },
        "Er Chele Vara": {
            "preliminares": [8.5, 8.6, 8.7, 8.9],
            "cuartos": [8.9, 8.8, 8.6, 8.7]
        }
    },
    "comparsas": {
        "Los Ángeles Caídos": {
            "preliminares": [9.5, 9.6, 9.7, 9.8],
            "cuartos": [9.7, 9.6, 9.8, 9.9],
            "semifinal": [9.8, 9.9, 9.8, 9.9],
            "final": [9.9, 9.9, 9.8, 9.8]
        },
        "Los Millonarios": {
            "preliminares": [9.3, 9.4, 9.5, 9.6],
            "cuartos": [9.6, 9.5, 9.7, 9.8],
            "semifinal": [9.7, 9.6, 9.7, 9.8]
        }
    },
    "coros": {
        "La Trinidad": {
            "preliminares": [9.0, 9.1, 9.2, 9.3],
            "cuartos": [9.3, 9.4, 9.5, 9.6],
            "semifinal": [9.5, 9.6, 9.7, 9.8],
            "final": [9.7, 9.8, 9.9, 9.8]
        },
        "El Batallón Fletilla": {
            "preliminares": [8.8, 8.9, 9.0, 9.1],
            "cuartos": [9.0, 9.1, 9.2, 9.3],
            "semifinal": [9.2, 9.3, 9.4, 9.5]
        }
    },
    "cuartetos": {
        "Tres notas Musicales": {
            "preliminares": [9.2, 9.3, 9.1, 9.4],
            "cuartos": [9.4, 9.5, 9.3, 9.6],
            "semifinal": [9.5, 9.6, 9.7, 9.6],
            "final": [9.7, 9.8, 9.6, 9.7]
        },
        "Ser o no Ser": {
            "preliminares": [8.7, 8.8, 8.9, 8.6],
            "cuartos": [8.9, 9.0, 8.8, 8.9]
        }
    }
}

def calcula_media_puntuaciones(grupos, **kwargs):
    """
    Calcula la media de las puntuaciones de las agrupaciones del concuros de carnaval y muestra los resultados de dfomra organizada
    
    Parámetros:
        - grupos (dict): Diccionario con las modalidades, agrupaciones y sus puntuaciones
        - kwargs
            - ag (str, opcional): Nombre de la agrupacion a la que vamosa actualizar las puntuaciones
            - fase (str, opcional): Nombre de la fase a actualizar.
            - puntuaciones (list, opcional): Lista de puntucaiones adicionales para agregar a la fase.

    Return: 
        - dict: Diccionario con las agrupaciones y su media de puntuación total. 
    """

    resultado = {}

    ag_nombre = kwargs.get("ag", None)
    fase_nombre = kwargs.get("fase", None)
    puntuaciones_adicionales = kwargs.get("puntuaciones", None)

    print(f"\nResultados del Concurso COAC \n")

    for modalidad, agrupaciones in grupos.items():
        print(f"Modalidad: {modalidad.upper()}\n{'-' * (11+len(modalidad))}")

        for agrupacion, fases in agrupaciones.items():
            if ag_nombre and agrupacion.lower() == ag_nombre.lower():
                if fase_nombre in fases:
                    fases[fase_nombre].extend(puntuaciones_adicionales)
                else:
                    fases[fase_nombre] = puntuaciones_adicionales
            print(f"\nAgrupacion: {agrupacion}")
            medias_por_fase = []

            for fase, puntuaciones in fases.items():
                puntuaciones_redondeadas = list(
                    map(lambda x: round(x, 2), puntuaciones)
                )
                media_fase = sum(puntuaciones_redondeadas) / len(puntuaciones_redondeadas)
                medias_por_fase.append(media_fase)
                print(f" - {fase.capitalize()}: Media = {round(media_fase, 2)}\n")
                
            media_total = sum(medias_por_fase) / len(medias_por_fase)
            resultado[agrupacion] = round(media_total, 2)

            print(f"\nMEDIA TOTAL: {round(media_total)}\n")
        print("\n" + "=" * 50 + "\n")
    print(resultado)    

# Ejemplo de uso:
calcula_media_puntuaciones(grupos)
# calcula_media_puntuaciones(grupos, ag="Los yesterday")
# calcula_media_puntuaciones(grupos)
