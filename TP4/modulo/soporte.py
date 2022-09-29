import os.path
import random
import pickle

class Proyecto:
    def __init__(self, nom, repo, actu, leng, likes, tags, url):
        self.nombre_usuario = nom
        self.repositorio = repo
        self.fecha_actualizacion = actu
        self.lenguaje = leng
        self.likes = likes
        self.tags = tags
        self.url = url


def leer(arreglo):
    print(f'Nombre de Usuario: {arreglo.nombre_usuario}', end='- ')
    print(f'Repositorio: {arreglo.repositorio}', end='- ')
    print(f'Fecha de Actualizacion {arreglo.fecha_actualizacion}', end='- ')
    print(f'Lenguaje: {arreglo.lenguaje}', end='- ')
    print(f'Likes: {arreglo.likes}', end='- ')
    print(f'Tags: {arreglo.tags}', end='- ')
    print(f'URL: {arreglo.url}')


def cargar_archivo(fd):
    m = open(fd, mode="rt", encoding="utf8")

    while True:
        line = m.readline()

        if line == '':
            break

        if line[-1] == '\n':
            line = line[:-1]

        print(line)

    m.flush()
    m.close()


