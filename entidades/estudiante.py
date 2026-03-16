from entidades.persona import Persona


class Estudiante(Persona):
    """
    Representa un estudiante en el sistema escolar.

    Hereda de Persona y añade atributos académicos como grado,
    salón, carnet y manejo de notas.

    Attributes:
        carnet (str): Identificador de carnet del estudiante.
        grado (str): Grado académico en el que se encuentra.
        salon (str): Salón al que pertenece el estudiante.
        cantidad_notas (int): Número máximo de notas permitidas.
        notas (list[float]): Lista de notas registradas.
    """

    def __init__(
        self,
        nombre: str,
        documento: str,
        edad: int,
        grado: str,
        salon: str,
        cantidad_notas: int,
        correo: str,
        carnet: str,
    ) -> None:
        """
        Inicializa un estudiante con sus datos personales y académicos.

        Args:
            nombre (str): Nombre completo del estudiante.
            documento (str): Número de documento de identidad.
            edad (int): Edad del estudiante.
            grado (str): Grado académico del estudiante.
            salon (str): Salón asignado al estudiante.
            cantidad_notas (int): Cantidad máxima de notas a registrar.
            correo (str): Correo electrónico del estudiante.
            carnet (str): Número de carnet del estudiante.
        """
        super().__init__(nombre, documento, edad, correo)
        self.carnet: str = carnet
        self.grado: str = grado
        self.salon: str = salon
        self.cantidad_notas: int = cantidad_notas
        self.notas: list[float] = []

    def registrar_nota(self, nota: float) -> str:
        if nota < 0.0 or nota > 5.0:
            return "La nota debe estar entre 0.0 y 5.0"

        if len(self.notas) >= self.cantidad_notas:
            return "Ya se registraron todas las notas"

        self.notas.append(nota)
        return "Nota registrada"

    def calcular_promedio(self) -> float:
        if len(self.notas) == 0:
            return 0.0
        return sum(self.notas) / len(self.notas)
