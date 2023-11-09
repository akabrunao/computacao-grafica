class Vec3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        """
        Soma dois vetores.
        
        Args:
            other (Vec3): vetor a ser somado
            
        Returns:
            Vec3: vetor resultante da soma
        """
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """
        Subtrai dois vetores.

        Args:
            other (Vec3): vetor a ser subtraído

        Returns:
            Vec3: vetor resultante da subtração
        """
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        """
        Multiplica um vetor por um escalar.

        Args:
            scalar (float): escalar a ser multiplicado

        Returns:
            Vec3: vetor resultante da multiplicação
        """
        return Vec3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __truediv__(self, scalar):
        """
        Divide um vetor por um escalar.

        Args:
            scalar (float): escalar a ser dividido

        Returns:
            Vec3: vetor resultante da divisão

        Raises:
            ValueError: divisão por zero
        """
        if scalar != 0:
            return Vec3(self.x / scalar, self.y / scalar, self.z / scalar)
        else:
            raise ValueError("Division by zero is not allowed.")

    def __str__(self):
        """
        Retorna uma string representando o vetor.

        Returns:
            str: string representando o vetor
        """
        return f"({self.x}, {self.y}, {self.z})"
