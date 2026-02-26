from entidades.persona import Persona


class Profesor(Persona):
    """
    Representa un profesor en el sistema escolar.

    Hereda de Persona y añade el atributo de especialidad.

    Attributes:
        especialidad (str): Área de especialidad del profesor.
    """

    def __init__(
        self,
        nombre: str,
        documento: str,
        edad: int,
        especialidad: str,
        correo: str,
    ) -> None:
        """
        Inicializa un profesor con sus datos personales y especialidad.

        Args:
            nombre (str): Nombre completo del profesor.
            documento (str): Número de documento de identidad.
            edad (int): Edad del profesor.
            especialidad (str): Área de especialidad del profesor.
            correo (str): Correo electrónico del profesor.
        """
        super().__init__(nombre, documento, edad, correo)
        self.especialidad: str = especialidad
