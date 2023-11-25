import unittest2
from objLoader import ObjLoader

class TestObjLoader(unittest2.TestCase):
    def test_loading(self):
        obj_loader = ObjLoader('Atividade03/Gato.obj')

        self.assertNotEqual(len(obj_loader.get_vertices()), 0)
        self.assertNotEqual(len(obj_loader.get_normals()), 0)
        self.assertNotEqual(len(obj_loader.get_faces()), 0)

if __name__ == '__main__':
    unittest2.main()
