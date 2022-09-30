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


def repos():
    vector_repositorio = []
    repositorio_sin_repetir = []

    if os.path.exists('proyectos.csv'):
        m = open('proyectos.csv', mode="rt", encoding="utf8")
        for i in m:
            token = i.split('|')
            repositorio = token[1]
            vector_repositorio.append(repositorio)

        for i in vector_repositorio:
            if not (i in repositorio_sin_repetir):
                repositorio_sin_repetir.append(i)

        m.flush()
        m.close()

        return repositorio_sin_repetir  # [A, B, C]


def cargar_archivo(fd, rep):
    ind = 0
    vector = []
    matriz = []
    if os.path.exists(fd):
        m = open(fd, mode="rt", encoding="utf8")
        t = os.path.getsize(fd)

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

                    v = Proyecto(nombre, repositorio, descripcion, fecha, lenguaje, likes, tags, url)
                    vector.append(v)

            else:
                pass

            ind += 1

        m.flush()
        m.close()

        return vector


def contar_lenguajes(fd):
    v = []
    ind = 0
    m = open(fd, 'rt')
    for line in m:
        token = line.split('|')
        if ind != 0:
            leng = token[4]
            if leng != '':
                if not (leng in v):
                    v.append(leng)
                else:
                    pass
        ind += 1
    return v


def proyectos_por_lenguaje(arreglo, leng):
    n = len(leng)
    acu = [0] * n

    for line in arreglo:
        if line.lenguaje in leng:
            acu[leng.index(line.lenguaje)] += 1

    n = len(acu)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if acu[i] < acu[j]:
                acu[i], acu[j] = acu[j], acu[i]
                leng[i], leng[j] = leng[j], leng[i]

    txt = '{:^10} | {:>30}'.format('Cantidad', 'Lenguaje')
    print(txt)

    for i in range(len(acu)):
        tabla = '{:^10} | {:>30}'.format(acu[i], leng[i])
        print(tabla)
