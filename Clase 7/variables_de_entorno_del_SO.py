import platform
import os


def mostrar_variables_entorno():
    print("=" * 60)
    print("INFORMACION BASICA DEL SISTEMA")
    print("=" * 60)
    print(
        f"Usuario del sistema: {os.environ.get('USERNAME') or os.environ.get('USER', 'No disponible')}"
    )
    print(f"Nombre del OS (os.name): {os.name}")
    print(f"Sistema Operativo: {platform.system()}")
    print(f"Version del sistema: {platform.version()}")
    print(f"Arquitectura: {platform.machine()}")
    print()

    variables_comunes = {
        "USERNAME": "Nombre de usuario (Windows)",
        "USERPROFILE": "Perfil del usuario (Windows)",
        "PATH": "Rutas de búsqueda de ejecutables",
        "TEMP": "Directorio temporal",
    }

    for var, descripcion in variables_comunes.items():
        valor = os.environ.get(var)
        # Truncar PATH si es muy largo para mejor visualización
        if var == "PATH":
            rutas = valor.split(os.pathsep) if valor else []
            print(f"{var:20} = {len(rutas)} rutas encontradas")
            if rutas:
                primeras_3 = rutas[:8]
                print(f"{'':20}   (Primeras 3: {', '.join(primeras_3)}...)")
        else:
            print(f"{var:20} = {valor[:88]}")

    variables_windows = {
        "COMPUTERNAME": "Nombre del equipo",
        "OS": "Tipo de sistema operativo",
        "HOMEDRIVE": "Unidad del directorio home",
        "HOMEPATH": "Ruta del directorio home",
        "APPDATA": "Directorio de datos de aplicación",
        "LOCALAPPDATA": "Directorio de datos locales",
        "PROGRAMFILES": "Directorio de archivos de programa",
        "PROGRAMFILES(X86)": "Directorio de archivos de programa (32 bits)",
        "SYSTEMROOT": "Directorio raíz del sistema",
        "WINDIR": "Directorio de Windows",
        "PUBLIC": "Directorio público",
        "SESSIONNAME": "Nombre de la sesión",
    }

    for var, descripcion in variables_windows.items():
        print(f"{var:20} = {os.environ.get(var)}")


if __name__ == "__main__":
    mostrar_variables_entorno()
