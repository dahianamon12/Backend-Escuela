class Persona:
    """
    Representa una persona en el sistema escolar.

    Es la clase base para Estudiante y Profesor, contiene
    los atributos comunes a cualquier persona.

    Attributes:
        nombre (str): Nombre completo de la persona.
        documento (str): Número de documento de identidad.
        edad (int): Edad de la persona.
        correo (str): Correo electrónico de la persona.
    """

    def __init__(self, nombre: str, documento: str, edad: int, correo: str) -> None:
        """
        Inicializa una persona con sus datos básicos.

        Args:
            nombre (str): Nombre completo de la persona.
            documento (str): Número de documento de identidad.
            edad (int): Edad de la persona.
            correo (str): Correo electrónico de la persona.
        """

        self.nombre: str = nombre
        self.documento: str = documento
        self.edad: int = edad
        self.correo: str = correo

    def mostrar_datos(self) -> str:
        """
        Retorna una cadena con los datos de la persona.

        Returns:
            str: Cadena con nombre, documento, edad y correo.
        """
        return f"Nombre: {self.nombre}, Documento: {self.documento}, Edad: {self.edad}, Correo:{self.correo}"
