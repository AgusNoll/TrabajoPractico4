import os.path
import random
import pickle


class Proyecto:
    def __init__(self, nom, repo, desc, actu, leng, likes, tags, url):
        self.nombre_usuario = nom
        self.repositorio = repo
        self.descripcion = desc
        self.fecha_actualizacion = actu
        self.lenguaje = leng
        self.likes = likes
        self.tags = tags
        self.url = url


class Fecha:
    def __init__(self, a, m, d):
        self.year = a
        self.mes = m
        self.dia = d


def leer(arreglo):
    print(f'Nombre de Usuario: {arreglo.nombre_usuario}', end='- ')
    print(f'Repositorio: {arreglo.repositorio}', end='- ')
    print(f'Fecha de Actualizacion {arreglo.fecha_actualizacion}', end='- ')
    print(f'Lenguaje: {arreglo.lenguaje}', end='- ')
    print(f'Likes: {arreglo.likes}', end='- ')
    print(f'Tags: {arreglo.tags}', end='- ')
    print(f'URL: {arreglo.url}')


def repos():
    vector_repositorio = []
    repo_sin_repetir = []

    if os.path.exists('proyectos.csv'):
        m = open('proyectos.csv', mode="rt", encoding="utf8")
        for i in m:
            token = i.split('|')
            repositorio = token[1]
            vector_repositorio.append(repositorio)

        for i in vector_repositorio:
            if not(i in repo_sin_repetir):
                repo_sin_repetir.append(i)

        m.flush()
        m.close()

        return repo_sin_repetir  # [A, B, C]


def cargar_archivo(fd, rep):
    ind = 0
    vector = []

    if os.path.exists(fd):
        m = open(fd, mode="rt", encoding="utf8")

        for line in m:
            token = line.split('|')

            if ind != 0:
                # repositorio [A, B, C, B, C]
                if token[1] in rep:  # [A, B, C]
                    rep.remove(token[1])

                    nombre = str(token[0])
                    repositorio = str(token[1])
                    descripcion = str(token[2])
                    fecha = str(token[3])  # Cree el Objeto Fecha, pero no sé cómo implementarlo
                    lenguaje = str(token[4])
                    likes = token[5]
                    likes = float(likes[:-1])

                    if token[6] != '':
                        tag = token[6]
                        token_tag = tag.split(',')
                        tags = token_tag

                    url = str(token[7])



                    #v = Proyecto(nombre, repositorio, descripcion, fecha, lenguaje, likes, tags, url)
                    #vector.append(v)

            else:
                pass

            ind += 1

        m.flush()
        m.close()

        return vector
