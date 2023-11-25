import numpy as np

class ObjLoader:
    """
    Classe para carregar dados de arquivos .obj e armazená-los para uso em gráficos 3D.

    A classe lê um arquivo .obj e extrai informações sobre vértices, normais e faces.
    Esses dados podem ser usados posteriormente para renderizar geometria 3D ou realizar
    outras operações relacionadas a gráficos 3D.

    Parâmetros:
    file_path (str): O caminho do arquivo .obj que será carregado.

    Atributos:
    vertices (list): Uma lista de vértices representados como listas de coordenadas (x, y, z).
    normals (list): Uma lista de normais representadas como listas de vetores (x, y, z).
    faces (list): Uma lista de faces, onde cada face é representada como uma lista de índices
        para vértices e normais.

    Métodos públicos:
    get_vertices(): Retorna a lista de vértices.
    get_normals(): Retorna a lista de normais.
    get_faces(): Retorna a lista de faces.

    Exemplo de uso:
    obj_loader = ObjLoader('seuarquivo.obj')
    vertices = obj_loader.get_vertices()
    normals = obj_loader.get_normals()
    faces = obj_loader.get_faces()
    """

    def __init__(self, file_path):
        """
        Inicializa a classe ObjLoader e carrega dados do arquivo .obj especificado.

        Parâmetros:
        file_path (str): O caminho do arquivo .obj que será carregado.
        """
        self.vertices = []
        self.normals = []
        self.faces = []

        with open(file_path, 'r') as file:
            for line in file:
                tokens = line.strip().split()
                if not tokens:
                    continue

                if tokens[0] == 'v':
                    # Processa informações de vértices
                    vertex = [float(tokens[1]), float(tokens[2]), float(tokens[3])]
                    self.vertices.append(vertex)
                elif tokens[0] == 'vn':
                    # Processa informações de normais
                    normal = [float(tokens[1]), float(tokens[2]), float(tokens[3])]
                    self.normals.append(normal)
                elif tokens[0] == 'f':
                    # Processa informações de faces
                    face = []
                    for token in tokens[1:]:
                        vertex_data = token.split('/')
                        vertex_index = int(vertex_data[0]) - 1
                        normal_index = int(vertex_data[2]) - 1
                        face.append((vertex_index, normal_index))
                    self.faces.append(face)

    def get_vertices(self):
        """
        Retorna a lista de vértices carregada do arquivo .obj.

        Retorna:
        list: Lista de vértices, onde cada vértice é representado como uma lista de coordenadas (x, y, z).
        """
        return self.vertices

    def get_normals(self):
        """
        Retorna a lista de normais carregada do arquivo .obj.

        Retorna:
        list: Lista de normais, onde cada normal é representada como uma lista de vetores (x, y, z).
        """
        return self.normals

    def get_faces(self):
        """
        Retorna a lista de faces carregada do arquivo .obj.

        Retorna:
        list: Lista de faces, onde cada face é representada como uma lista de índices para vértices e normais.
        """
        return self.faces
