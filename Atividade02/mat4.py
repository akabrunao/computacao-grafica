class Mat4:
    def __init__(self, m11=1, m12=0, m13=0, m14=0, m21=0, m22=1, m23=0, m24=0, m31=0, m32=0, m33=1, m34=0, m41=0, m42=0, m43=0, m44=1):
        self.m11 = m11
        self.m12 = m12
        self.m13 = m13
        self.m14 = m14
        self.m21 = m21
        self.m22 = m22
        self.m23 = m23
        self.m24 = m24
        self.m31 = m31
        self.m32 = m32
        self.m33 = m33
        self.m34 = m34
        self.m41 = m41
        self.m42 = m42
        self.m43 = m43
        self.m44 = m44

    def __mul__(self, other):
        """
        Multiplicação de matrizes 4x4

        Args:
            other (Mat4): matriz a ser multiplicada

        Returns:
            Mat4: matriz resultante da multiplicação
        """
        if isinstance(other, Mat4):
            # Multiplicação de matrizes 4x4
            result = Mat4()
            for i in range(4):
                for j in range(4):
                    total = 0
                    for k in range(4):
                        total += getattr(self, f'm{i+1}{k+1}') * getattr(other, f'm{k+1}{j+1}')
                    setattr(result, f'm{i+1}{j+1}', total)
            return result
        elif isinstance(other, (int, float)):
            # Multiplicação por um escalar
            return Mat4(
                self.m11 * other, self.m12 * other, self.m13 * other, self.m14 * other,
                self.m21 * other, self.m22 * other, self.m23 * other, self.m24 * other,
                self.m31 * other, self.m32 * other, self.m33 * other, self.m34 * other,
                self.m41 * other, self.m42 * other, self.m43 * other, self.m44 * other
            )

    def __str__(self):
        """
        Retorna uma string representando a matriz

        Returns:
            str: string representando a matriz
        """
        return f"[[{self.m11}, {self.m12}, {self.m13}, {self.m14}], " \
               f"[{self.m21}, {self.m22}, {self.m23}, {self.m24}], " \
               f"[{self.m31}, {self.m32}, {self.m33}, {self.m34}], " \
               f"[{self.m41}, {self.m42}, {self.m43}, {self.m44}]]"
