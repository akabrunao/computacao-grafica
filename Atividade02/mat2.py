class Mat2:
    def __init__(self, m11=1, m12=0, m21=0, m22=1):
        self.m11 = m11
        self.m12 = m12
        self.m21 = m21
        self.m22 = m22

    def __mul__(self, other):
        """
        Multiplicação de matrizes 2x2

        Args:
            other (Mat2): matriz a ser multiplicada

        Returns:
            Mat2: matriz resultante da multiplicação
        """
        if isinstance(other, Mat2):
            # Multiplicação de matrizes 2x2
            result = Mat2()
            result.m11 = self.m11 * other.m11 + self.m12 * other.m21
            result.m12 = self.m11 * other.m12 + self.m12 * other.m22
            result.m21 = self.m21 * other.m11 + self.m22 * other.m21
            result.m22 = self.m21 * other.m12 + self.m22 * other.m22
            return result
        elif isinstance(other, (int, float)):
            # Multiplicação por um escalar
            return Mat2(self.m11 * other, self.m12 * other, self.m21 * other, self.m22 * other)

    def __str__(self):
        """
        Retorna uma string representando a matriz

        Returns:
            str: string representando a matriz
        """
        return f"[[{self.m11}, {self.m12}], [{self.m21}, {self.m22}]]"
