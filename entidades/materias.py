class Materia:
    def __init__(
        self,
        codigo: str,
        nombre: str,
        modalidad: str,
        intensidad_horas_sem: int,
        cantidad_sem: int,
    ) -> None:

        self._codigo = codigo.strip()
        self._nombre = nombre.strip()
        self._modalidad = modalidad.strip().lower()
        self._intensidad_horas_sem = intensidad_horas_sem
        self._cantidad_sem = cantidad_sem

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def modalidad(self) -> str:
        return self._modalidad

    @property
    def intensidad_horas_sem(self) -> int:
        return self._intensidad_horas_sem

    @property
    def cantidad_sem(self) -> int:
        return self._cantidad_sem

    def validar_materias(self) -> bool:

        if not self._codigo:
            return False

        if not self._nombre:
            return False

        validar_modalidad = {"presencial", "virtual", "mixta"}
        if self._modalidad not in validar_modalidad:
            return False

        if self._intensidad_horas_sem <= 0:
            return False

        if self._cantidad_sem <= 0:
            return False

        return True

    def __str__(self) -> str:

        return (
            f"{self._nombre} con el codigo: "
            f"{self._codigo} en modalidad "
            f"{self._modalidad}, intensidad de "
            f"{self._intensidad_horas_sem} horas semanales y duración de "
            f"{self._cantidad_sem} semanas."
        )
