from entidades.persona import Persona


class Estudiante(Persona):
    def __init__(
        self,
        nombre: str,
        documento: str,
        edad: int,
        grado: str,
        salon: str,
        cantidad_notas: int,
        correo: str,
    ) -> None:
        super().__init__(nombre, documento, edad, correo)
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
