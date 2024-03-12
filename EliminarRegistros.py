import os

def eliminar_archivo_resultados():
    nombre_archivo = "resultados.db" 

    if os.path.exists(nombre_archivo):
        os.remove(nombre_archivo)
        print(f"La base {nombre_archivo} ha sido eliminada.")
    else:
        print(f"No hay ninguna base de datos para eliminar.")