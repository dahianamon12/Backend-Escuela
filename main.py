from entidades.estudiante import Estudiante
from entidades.profesor import Profesor
from entidades.materias import Materia


def menu() -> None:
    """
    Muestra en pantalla el menú principal del sistema escolar
    con las opciones disponibles para el usuario.
    """
    print("\n-----Sistema Escolar-----")
    print("1. Registrar estudiante")
    print("2. Registrar profesor")
    print("3. Registrar materia")
    print("4. Registrar nota a estudiante")
    print("5. Calcular promedio a estudiante")
    print("6. Listar a estudiante")
    print("7. Listar profesores")
    print("8. Listar materias")
    print("9. Salir")


def registrar_materia(lista_materias: list) -> None:
    """
    Solicita al usuario los datos de una materia, crea una instancia
    de la clase Materia y la agrega a la lista si los datos son válidos.

    Args:
        lista_materias (list): Lista donde se almacenan las materias registradas.

    Returns:
        None
    """
    codigo = input("Ingrese el codigo del grupo que desea crear: ")
    nombre = input("Nombre: ")
    modalidad = input("Modalidad entre 'presencial', 'virtual' o 'mixta': ")
    intensidad_horas_sem = int(
        input("La cantidad de horas a la semana que se ve la materia: ")
    )
    cantidad_sem = int(input("Numero de semanas que dura la materia: "))

    materia = Materia(codigo, nombre, modalidad, intensidad_horas_sem, cantidad_sem)

    if materia.validar_materias():
        lista_materias.append(materia)
        print("Materia registrada correctamente.")
    else:
        print("No se puede registrar la materia, datos invalidos.")


def mostrar_materias(lista_materias: list) -> None:
    """
    Muestra en pantalla todas las materias registradas.

    Si la lista está vacía, informa que no hay materias registradas.

    Args:
        lista_materias (list): Lista que contiene las materias registradas.

    Returns:
        None
    """
    if not lista_materias:
        print("Aun no hay materias registradas.")
        return
    for materia in lista_materias:
        print(materia)


def texto_no_vacio(texto: str) -> bool:
    return len(texto.strip()) > 0


def validar_entero(numero: str) -> tuple[bool, int]:
    numero = numero.strip()
    if not numero.isdigit():
        return False, 0
    return True, int(numero)


def validar_nota(nota_str: str) -> tuple[bool, float]:
    nota_str = nota_str.strip()
    partes = nota_str.split(".")

    if len(partes) > 2:
        return False, 0.0

    entero = partes[0]
    decimal = partes[1] if len(partes) == 2 else ""

    if not entero.isdigit():
        return False, 0.0

    if decimal != "" and not decimal.isdigit():
        return False, 0.0

    valor = float(nota_str)

    if valor < 0.0 or valor > 5.0:
        return False, 0.0

    return True, valor


def main() -> None:
    estudiantes: dict[str, Estudiante] = {}
    profesores: dict[str, Profesor] = {}
    materias = []

    while True:
        menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
            print("Opcion invalida")
            continue

        if opcion == "1":  # FIX: todo el bloque ahora está dentro del if
            documento = input("Documento: ").strip()

            if documento in estudiantes:
                print("Ya existe un estudiante con ese documento.")
                continue

            nombre = input("Nombre: ").strip()
            if not texto_no_vacio(nombre):
                print("Nombre inválido.")
                continue

            edad_str = input("Edad: ")
            ok_edad, edad = validar_entero(edad_str)
            if not ok_edad:
                print("Edad inválida.")
                continue

            correo = input("Correo: ").strip()
            if not texto_no_vacio(correo):
                print("Correo inválido.")
                continue

            carnet = input("Carnet: ").strip()
            if not texto_no_vacio(carnet):
                print("Carnet inválido.")
                continue

            grado = input("Grado: ").strip()
            salon = input("Salón: ").strip()

            cantidad_str = input("Cantidad de notas: ")
            ok_cant, cantidad = validar_entero(cantidad_str)
            if not ok_cant or cantidad <= 0:
                print("Cantidad inválida.")
                continue

            estudiantes[documento] = Estudiante(
                nombre,
                documento,
                edad,
                correo,
                carnet,
                grado,
                salon,
                cantidad,
            )
            print("Estudiante registrado correctamente.")

        elif opcion == "2":
            documento = input("Documento: ").strip()

            if documento in profesores:
                print("Ya existe un profesor con ese documento.")
                continue

            nombre = input("Nombre: ").strip()
            if not texto_no_vacio(nombre):
                print("Nombre inválido.")
                continue

            edad_str = input("Edad: ")
            ok_edad, edad = validar_entero(edad_str)
            if not ok_edad:
                print("Edad inválida.")
                continue

            correo = input("Correo: ").strip()
            if not texto_no_vacio(correo):
                print("Correo inválido.")
                continue

            especialidad = input("Especialidad: ").strip()

            profesores[documento] = Profesor(
                nombre,
                documento,
                edad,
                correo,
                especialidad,
            )
            print("Profesor registrado correctamente.")

        elif opcion == "3":
            registrar_materia(materias)

        elif opcion == "4":
            documento = input("Documento del estudiante: ").strip()

            if documento not in estudiantes:
                print("Estudiante no existe.")
                continue

            nota_str = input("Nota (0.0 - 5.0): ")
            ok_nota, nota = validar_nota(nota_str)
            if not ok_nota:
                print("Nota inválida.")
                continue

            print(estudiantes[documento].registrar_nota(nota))

        elif opcion == "5":
            documento = input("Documento del estudiante: ").strip()

            if documento not in estudiantes:
                print("Estudiante no existe.")
                continue

            promedio = estudiantes[documento].calcular_promedio()
            print(f"Promedio actual: {promedio:.2f}")

        elif opcion == "6":
            if not estudiantes:
                print("No hay estudiantes registrados.")
                continue

            for est in estudiantes.values():
                print(est.mostrar_datos())

        elif opcion == "7":
            if not profesores:
                print("No hay profesores registrados.")
                continue

            for profesor in profesores.values():
                print(profesor.mostrar_datos())

        elif opcion == "8":
            mostrar_materias(materias)

        elif opcion == "9":
            print("Saliendo del sistema...")
            break


if __name__ == "__main__":
    main()
