class Vec2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        """
        Soma de vetores

        Args:
            other (Vec2): vetor a ser somado

        Returns:
            Vec2: vetor resultante da soma
        """
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """
        Subtração de vetores

        Args:
            other (Vec2): vetor a ser subtraído

        Returns:
            Vec2: vetor resultante da subtração
        """
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """
        Multiplicação de vetor por escalar

        Args:
            scalar (float): escalar a ser multiplicado

        Returns:
            Vec2: vetor resultante da multiplicação
        """
        return Vec2(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        """
        Divisão de vetor por escalar

        Args:
            scalar (float): escalar a ser dividido

        Returns:
            Vec2: vetor resultante da divisão

        Raises:
            ValueError: divisão por zero
        """
        if scalar != 0:
            return Vec2(self.x / scalar, self.y / scalar)
        else:
            raise ValueError("Division by zero is not allowed.")

    def __str__(self):
        """
        Representação em string do vetor

        Returns:
            str: representação em string do vetor
        """
        return f"({self.x}, {self.y})"
