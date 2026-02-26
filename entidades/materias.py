class Materia:
    def __init__(
        self,
        codigo: str,
        nombre: str,
        modalidad: str,
        intensidad_horas_sem: int,
        cantidad_sem: int,
    ) -> None:
        """
        Inicializa una nueva instancia de la clase Materia.

        Args:
            codigo (str): Código identificador único de la materia.
            nombre (str): Nombre de la materia.
            modalidad (str): Modalidad en la que se dicta la materia
                (por ejemplo: presencial, virtual o híbrida).
            intensidad_horas_sem (int): Número de horas semanales de la materia.
            cantidad_sem (int): Cantidad de semestres en los que se ofrece
                o pertenece la materia.
            modalidad (str): Modalidad de la materia.
            Se almacena en minúsculas y sin espacios extra.
        """

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
        """
        Valida que los atributos de la materia cumplan con las reglas establecidas.

        Reglas de validación:
            - El código no debe estar vacío.
            - El nombre no debe estar vacío.
            - La modalidad debe ser "presencial", "virtual" o "mixta".
            - La intensidad horaria semanal debe ser mayor que 0.
            - La cantidad de semestres debe ser mayor que 0.

        Returns:
            bool: True si todos los datos son válidos, False en caso contrario.
        """
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
        """
        Valida que los atributos de la materia cumplan con las reglas establecidas.

        Reglas de validación:
            - El código no debe estar vacío.
            - El nombre no debe estar vacío.
            - La modalidad debe ser "presencial", "virtual" o "mixta".
            - La intensidad horaria semanal debe ser mayor que 0.
            - La cantidad de semestres debe ser mayor que 0.

        Returns:
            bool: True si todos los datos son válidos, False en caso contrario.
        """
        return (
            f"{self._nombre} con el codigo: "
            f"{self._codigo} en modalidad "
            f"{self._modalidad}, intensidad de "
            f"{self._intensidad_horas_sem} horas semanales y duración de "
            f"{self._cantidad_sem} semanas."
        )
