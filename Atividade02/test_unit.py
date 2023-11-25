# Para testar:
# rode 'python3 ./Atividade02/test_unit.py' no terminal


import unittest2
from vec2 import Vec2
from vec3 import Vec3
from vec4 import Vec4
from mat2 import Mat2
from mat3 import Mat3
from mat4 import Mat4

class TestMat2(unittest2.TestCase):
    def test_matrix_multiplication(self):
        mat1 = Mat2(1, 2, 3, 4)
        mat2 = Mat2(5, 6, 7, 8)
        result = mat1 * mat2
        expected_result = Mat2(19, 22, 43, 50)
        self.assertEqual(result.m11, expected_result.m11)
        self.assertEqual(result.m12, expected_result.m12)
        self.assertEqual(result.m21, expected_result.m21)
        self.assertEqual(result.m22, expected_result.m22)

    def test_scalar_multiplication(self):
        mat = Mat2(1, 2, 3, 4)
        scalar = 2
        result = mat * scalar
        expected_result = Mat2(2, 4, 6, 8)
        self.assertEqual(result.m11, expected_result.m11)
        self.assertEqual(result.m12, expected_result.m12)
        self.assertEqual(result.m21, expected_result.m21)
        self.assertEqual(result.m22, expected_result.m22)

    def test_matrix_string_representation(self):
        mat = Mat2(1, 2, 3, 4)
        expected_string = "[[1, 2], [3, 4]]"
        self.assertEqual(str(mat), expected_string)



class TestMat3(unittest2.TestCase):
    def test_matrix_multiplication(self):
        mat1 = Mat3(1, 2, 3, 4, 5, 6, 7, 8, 9)
        mat2 = Mat3(9, 8, 7, 6, 5, 4, 3, 2, 1)
        result = mat1 * mat2
        expected_result = Mat3(30, 24, 18, 84, 69, 54, 138, 114, 90)
        self.assertEqual(result.m11, expected_result.m11)
        self.assertEqual(result.m12, expected_result.m12)
        self.assertEqual(result.m13, expected_result.m13)
        self.assertEqual(result.m21, expected_result.m21)
        self.assertEqual(result.m22, expected_result.m22)
        self.assertEqual(result.m23, expected_result.m23)
        self.assertEqual(result.m31, expected_result.m31)
        self.assertEqual(result.m32, expected_result.m32)
        self.assertEqual(result.m33, expected_result.m33)

    def test_scalar_multiplication(self):
        mat = Mat3(1, 2, 3, 4, 5, 6, 7, 8, 9)
        scalar = 2
        result = mat * scalar
        expected_result = Mat3(2, 4, 6, 8, 10, 12, 14, 16, 18)
        self.assertEqual(result.m11, expected_result.m11)
        self.assertEqual(result.m12, expected_result.m12)
        self.assertEqual(result.m13, expected_result.m13)
        self.assertEqual(result.m21, expected_result.m21)
        self.assertEqual(result.m22, expected_result.m22)
        self.assertEqual(result.m23, expected_result.m23)
        self.assertEqual(result.m31, expected_result.m31)
        self.assertEqual(result.m32, expected_result.m32)
        self.assertEqual(result.m33, expected_result.m33)

    def test_matrix_string_representation(self):
        mat = Mat3(1, 2, 3, 4, 5, 6, 7, 8, 9)
        expected_string = "[[1, 2, 3], [4, 5, 6], [7, 8, 9]]"
        self.assertEqual(str(mat), expected_string)



    
class TestMat4(unittest2.TestCase):
    def test_matrix_multiplication(self):
        mat1 = Mat4(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
        mat2 = Mat4(16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
        result = mat1 * mat2
        expected_result = Mat4(80, 70, 60, 50, 240, 214 ,188, 162, 400, 358, 316, 274, 560, 502, 444, 386)
        self.assertEqual(result.m11, expected_result.m11)
        self.assertEqual(result.m12, expected_result.m12)
        self.assertEqual(result.m13, expected_result.m13)
        self.assertEqual(result.m14, expected_result.m14)
        self.assertEqual(result.m21, expected_result.m21)
        self.assertEqual(result.m22, expected_result.m22)
        self.assertEqual(result.m23, expected_result.m23)
        self.assertEqual(result.m24, expected_result.m24)
        self.assertEqual(result.m31, expected_result.m31)
        self.assertEqual(result.m32, expected_result.m32)
        self.assertEqual(result.m33, expected_result.m33)
        self.assertEqual(result.m34, expected_result.m34)
        self.assertEqual(result.m41, expected_result.m41)
        self.assertEqual(result.m42, expected_result.m42)
        self.assertEqual(result.m43, expected_result.m43)
        self.assertEqual(result.m44, expected_result.m44)

    def test_scalar_multiplication(self):
        mat = Mat4(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
        scalar = 2
        result = mat * scalar
        expected_result = Mat4(2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32)
        self.assertEqual(result.m11, expected_result.m11)
        self.assertEqual(result.m12, expected_result.m12)
        self.assertEqual(result.m13, expected_result.m13)
        self.assertEqual(result.m14, expected_result.m14)
        self.assertEqual(result.m21, expected_result.m21)
        self.assertEqual(result.m22, expected_result.m22)
        self.assertEqual(result.m23, expected_result.m23)
        self.assertEqual(result.m24, expected_result.m24)
        self.assertEqual(result.m31, expected_result.m31)
        self.assertEqual(result.m32, expected_result.m32)
        self.assertEqual(result.m33, expected_result.m33)
        self.assertEqual(result.m34, expected_result.m34)
        self.assertEqual(result.m41, expected_result.m41)
        self.assertEqual(result.m42, expected_result.m42)
        self.assertEqual(result.m43, expected_result.m43)
        self.assertEqual(result.m44, expected_result.m44)

    def test_matrix_string_representation(self):
        mat = Mat4(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
        expected_string = "[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]"
        self.assertEqual(str(mat), expected_string)




class TestVec2(unittest2.TestCase):
    def test_addition(self):
        vec1 = Vec2(1, 2)
        vec2 = Vec2(3, 4)
        result = vec1 + vec2
        expected_result = Vec2(4, 6)
        self.assertEqual(result.x, expected_result.x)
        self.assertEqual(result.y, expected_result.y)

    def test_subtraction(self):
        vec1 = Vec2(1, 2)
        vec2 = Vec2(3, 4)
        result = vec1 - vec2
        expected_result = Vec2(-2, -2)
        self.assertEqual(result.x, expected_result.x)
        self.assertEqual(result.y, expected_result.y)

    def test_scalar_multiplication(self):
        vec = Vec2(1, 2)
        scalar = 3
        result = vec * scalar
        expected_result = Vec2(3, 6)
        self.assertEqual(result.x, expected_result.x)
        self.assertEqual(result.y, expected_result.y)

    def test_scalar_division(self):
        vec = Vec2(3, 6)
        scalar = 3
        result = vec / scalar
        expected_result = Vec2(1, 2)
        self.assertEqual(result.x, expected_result.x)
        self.assertEqual(result.y, expected_result.y)

    def test_scalar_division_by_zero(self):
        vec = Vec2(1, 2)
        scalar = 0
        with self.assertRaises(ValueError):
            vec / scalar

    def test_string_representation(self):
        vec = Vec2(1, 2)
        expected_string = "(1, 2)"
        self.assertEqual(str(vec), expected_string)




class TestVec3(unittest2.TestCase):
    def test_addition(self):
        vec1 = Vec3(1, 2, 3)
        vec2 = Vec3(4, 5, 6)
        result = vec1 + vec2
        self.assertEqual(result.x, 5)
        self.assertEqual(result.y, 7)
        self.assertEqual(result.z, 9)

    def test_subtraction(self):
        vec1 = Vec3(1, 2, 3)
        vec2 = Vec3(4, 5, 6)
        result = vec1 - vec2
        self.assertEqual(result.x, -3)
        self.assertEqual(result.y, -3)
        self.assertEqual(result.z, -3)

    def test_multiplication(self):
        vec1 = Vec3(1, 2, 3)
        result = vec1 * 2
        self.assertEqual(result.x, 2)
        self.assertEqual(result.y, 4)
        self.assertEqual(result.z, 6)

    def test_division(self):
        vec1 = Vec3(1, 2, 3)
        result = vec1 / 2
        self.assertEqual(result.x, 0.5)
        self.assertEqual(result.y, 1.0)
        self.assertEqual(result.z, 1.5)

    def test_division_by_zero(self):
        vec1 = Vec3(1, 2, 3)
        with self.assertRaises(ValueError):
            vec1 / 0

    def test_string_representation(self):
        vec1 = Vec3(1, 2, 3)
        result = str(vec1)
        self.assertEqual(result, "(1, 2, 3)")




class TestVec4(unittest2.TestCase):
    def test_addition(self):
        vec1 = Vec4(1, 2, 3, 4)
        vec2 = Vec4(4, 5, 6, 7)
        result = vec1 + vec2
        self.assertEqual(result.x, 5)
        self.assertEqual(result.y, 7)
        self.assertEqual(result.z, 9)
        self.assertEqual(result.w, 11)

    def test_subtraction(self):
        vec1 = Vec4(1, 2, 3, 4)
        vec2 = Vec4(4, 5, 6, 7)
        result = vec1 - vec2
        self.assertEqual(result.x, -3)
        self.assertEqual(result.y, -3)
        self.assertEqual(result.z, -3)
        self.assertEqual(result.w, -3)

    def test_multiplication(self):
        vec1 = Vec4(1, 2, 3, 4)
        result = vec1 * 2
        self.assertEqual(result.x, 2)
        self.assertEqual(result.y, 4)
        self.assertEqual(result.z, 6)
        self.assertEqual(result.w, 8)

    def test_division(self):
        vec1 = Vec4(1, 2, 3, 4)
        result = vec1 / 2
        self.assertEqual(result.x, 0.5)
        self.assertEqual(result.y, 1.0)
        self.assertEqual(result.z, 1.5)
        self.assertEqual(result.w, 2.0)

    def test_division_by_zero(self):
        vec1 = Vec4(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            vec1 / 0

    def test_string_representation(self):
        vec1 = Vec4(1, 2, 3, 4)
        result = str(vec1)
        self.assertEqual(result, "(1, 2, 3, 4)")

    
if __name__ == '__main__':
    unittest2.main()