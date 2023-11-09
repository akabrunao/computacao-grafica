class Mat3:
    def __init__(self, m11=1, m12=0, m13=0, m21=0, m22=1, m23=0, m31=0, m32=0, m33=1):
        self.m11 = m11
        self.m12 = m12
        self.m13 = m13
        self.m21 = m21
        self.m22 = m22
        self.m23 = m23
        self.m31 = m31
        self.m32 = m32
        self.m33 = m33

    def __mul__(self, other):
        """
        Multiplicação de matrizes 3x3

        Args:
            other (Mat3): matriz a ser multiplicada

        Returns:
            Mat3: matriz resultante da multiplicação
        """
        if isinstance(other, Mat3):
            # Multiplicação de matrizes 3x3
            result = Mat3()
            result.m11 = self.m11 * other.m11 + self.m12 * other.m21 + self.m13 * other.m31
            result.m12 = self.m11 * other.m12 + self.m12 * other.m22 + self.m13 * other.m32
            result.m13 = self.m11 * other.m13 + self.m12 * other.m23 + self.m13 * other.m33
            result.m21 = self.m21 * other.m11 + self.m22 * other.m21 + self.m23 * other.m31
            result.m22 = self.m21 * other.m12 + self.m22 * other.m22 + self.m23 * other.m32
            result.m23 = self.m21 * other.m13 + self.m22 * other.m23 + self.m23 * other.m33
            result.m31 = self.m31 * other.m11 + self.m32 * other.m21 + self.m33 * other.m31
            result.m32 = self.m31 * other.m12 + self.m32 * other.m22 + self.m33 * other.m32
            result.m33 = self.m31 * other.m13 + self.m32 * other.m23 + self.m33 * other.m33
            return result
        elif isinstance(other, (int, float)):
            # Multiplicação por um escalar
            return Mat3(self.m11 * other, self.m12 * other, self.m13 * other,
                        self.m21 * other, self.m22 * other, self.m23 * other,
                        self.m31 * other, self.m32 * other, self.m33 * other)

    def __str__(self):
        """
        Retorna uma string representando a matriz

        Returns:
            str: string representando a matriz
        """
        return f"[[{self.m11}, {self.m12}, {self.m13}], [{self.m21}, {self.m22}, {self.m23}], [{self.m31}, {self.m32}, {self.m33}]]"
