from tabulate import tabulate
from actor_queries import get_actors, get_actors_dict, get_actor_films
from variables_de_entorno_del_SO import mostrar_variables_entorno
import os

print("ACA VAMOS A VER LAS VARIABLES DE ENTORNO DEL SO")
mostrar_variables_entorno()


actors = get_actors(limit=10)
headers = ["ID", "Nombre", "Apellido", "Fecha de contratación"]
print(tabulate(actors, headers=headers, tablefmt="fancy_grid"))

actor_name_0 = actors[0][1]
print(f"El nombre del primer actor es: {actor_name_0}")
os.system("cls")
actors = get_actors_dict(limit=10)

tabla_datos = []
for actor in actors:
    fila = [
        actor["actor_id"],
        actor["first_name"],
        actor["last_name"],
        actor["last_update"],
    ]
    tabla_datos.append(fila)

print(tabulate(tabla_datos, headers=headers, tablefmt="fancy_grid"))

actor_name_0 = actors[0]["first_name"]
print(f"El nombre del primer actor es: {actor_name_0}")

actor_id = actor_id=actors[2]["actor_id"]
films = get_actor_films(actor_id)

if films and len(films) > 0:
    tabla_datos = []
    for idx, film in enumerate(films, start=1):
        fila = [
            idx,                    # Número de orden
            film['title']          # Título de la película
        ]
        tabla_datos.append(fila)
    
    headers = ["#", f"Películas del actor ID {actor_id}"]
    
    print(tabulate(tabla_datos, headers=headers, tablefmt="fancy_grid"))
    print(f"\n✓ Total: {len(films)} películas encontradas")