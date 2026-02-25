class Persona:
    def __init__(self, nombre: str, documento: str, edad: int, correo: str) -> None:
        self.nombre: str = nombre
        self.documento: str = documento
        self.edad: int = edad
        self.correo: str = correo

    def mostrar_datos(self) -> str:
        return f"Nombre: {self.nombre}, Documento: {self.documento}, Edad: {self.edad}, Correo:{self.correo}"
