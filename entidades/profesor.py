from entidades.persona import Persona


class Profesor(Persona):
    def __init__(
        self,
        nombre: str,
        documento: str,
        edad: int,
        especialidad: str,
        correo: str,
    ) -> None:
        super().__init__(nombre, documento, edad, correo)
        self.especialidad: str = especialidad
