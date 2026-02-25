from entidades.estudiante import Estudiante
from entidades.profesor import Profesor
from entidades.materias import Materia


def menu() -> None:
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
    codigo = input("Ingrese el codigo del grupo que desea crear: ")
    nombre = input("Nombre: ")
    modalidad = input("Modalidad entre 'presencial', 'virtual' o 'mixta': ")
    intensidad_horas_sem = int(
        input("La cantidad de horas a la semana que se ve la materia: ")
    )
    cantidad_sem = int(input("Numero de sesmanas que dura la materia: "))

    materia = Materia(codigo, nombre, modalidad, intensidad_horas_sem, cantidad_sem)

    if materia.validar_materias():
        lista_materias.append(materia)
        print("Materia registrada correctamente.")
    else:
        print("No se puede registar la materia, datos invalidos.")


def mostrar_materias(lista_materias: list) -> None:
    if not lista_materias:
        print("Aun no hay materias registradas.")
        return
    for materia in lista_materias:
        print(materia)


def main() -> None:
    materias = []
    while True:
        menu()
        opcion = input("Selccione una opcion: ").strip()
        if opcion not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
            print("Opcion invalida")
            continue
        if opcion == "1":
            continue

        elif opcion == "2":
            continue
        elif opcion == "3":
            registrar_materia()

        elif opcion == "4":
            continue
        elif opcion == "5":
            continue
        elif opcion == "6":
            continue
        elif opcion == "7":
            continue
        elif opcion == "8":
            mostrar_materias()

        elif opcion == "9":
            print("Saliendo del sistem...")
            break


if __name__ == "_main_":
    main()
