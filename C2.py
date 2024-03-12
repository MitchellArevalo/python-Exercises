import os

def makeFoldersPeople(nameList):

    try:
        os.mkdir("moduloPersonas")
    except FileExistsError:
        pass

    for name in nameList:
        folder_name = "moduloPersonas/" + name
        try:
            os.mkdir(folder_name)
            print(f"Carpeta de {name} creada.")
        except FileExistsError:
            print(f"{name} ya tiene una carpeta.")


nombres = ["Pepe", "Juan", "María", "Luisa"]
makeFoldersPeople(nombres)