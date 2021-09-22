import json, os

def load_coordinates():
    '''Carrega arquivo com as coordenadas'''
    file_path = './utils/coordinates.json'

    if os.path.exists(file_path):
        f = open(file_path)
        coordinates = json.load(f)
        return coordinates

    raise ValueError(f'O arquivo "{ file_path }" não existe')