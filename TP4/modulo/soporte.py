import os.path
import datetime
import pickle
import os.path


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


def leer_stars(arreglo):

    if 0 < arreglo.likes <= 10.0:
        arreglo.likes = 1
    elif 10.1 < arreglo.likes <= 20.0:
        arreglo.likes = 2
    elif 20.1 < arreglo.likes <= 30.0:
        arreglo.likes = 3
    elif 30.1 < arreglo.likes <= 40.0:
        arreglo.likes = 4
    elif 40.1 <= arreglo.likes:
        arreglo.likes = 5

    txt = '{:<40} | {:^10} | {:^5}'.format(arreglo.repositorio, arreglo.fecha_actualizacion, arreglo.likes)
    print(txt)


class Matriz:
    def __init__(self, mes, estrellas, cant_proyectos):
        self.mes = mes
        self.estrellas = estrellas
        self.cant_proyectos = cant_proyectos


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


def add_in_arder(vector, reg): # ni idea como funciona esto, pero funciona.
    n = len(vector)
    izq, der = 0, n-1
    pos = n
    while izq <= der:
        c = (izq + der) // 2

        if vector[c].repositorio == reg.repositorio:
            pos = c
            break

        if vector[c].repositorio < reg.repositorio:
            izq = c + 1
        else:
            der = c - 1

    if izq > der:
        pos = izq

    vector[pos:pos] = [reg]


def likes_por_estrellas(arreglo):

    for i in range(len(arreglo)):

        if 0 < arreglo[i].likes <= 10.0:
            arreglo[i].likes = 1
        elif 10.1 < arreglo[i].likes <= 20.0:
            arreglo[i].likes = 2
        elif 20.1 < arreglo[i].likes <= 30.0:
            arreglo[i].likes = 3
        elif 30.1 < arreglo[i].likes <= 40.0:
            arreglo[i].likes = 4
        elif 40.1 <= arreglo[i].likes:
            arreglo[i].likes = 5


def cargar_archivo(fd, rep):
    ind = 0
    vector = []
    matriz = []
    if os.path.exists(fd):
        tags = ''
        m = open(fd, mode="rt", encoding="utf8")
        t = os.path.getsize(fd)

        for line in m:
            token = line.split('|')

            if ind != 0: # Condicional para que no cuente la primera línea

                if token[1] in rep: # Condicional para que los repositorios no se repitan

                    rep.remove(token[1])

                    nombre = str(token[0])
                    repositorio = str(token[1]).lower()
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
                    add_in_arder(vector, v)

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

    txt = '{:^10} | {:^20}'.format('Cantidad', 'Lenguaje')
    print(txt)

    for i in range(len(acu)):
        tabla = '{:^10} | {:<20}'.format(acu[i], leng[i])
        print(tabla)


def filtrar_tag(v):
    bandera = False

    if len(v) == 0:
        print('\nNo hay datos cargados...')
        print('Opcion "1. Cargar" para continuar')
        return

    tag_x = input('Ingrese un nuevo tag: ')
    print()
    fd = 'archivo_copia.csv'
    m = open(fd, 'wt')
    for i in range(len(v)):
        if tag_x in v[i].tags:

            leer_stars(v[i])
            bandera = True
            dat = str(v[i].nombre_usuario + '|' + v[i].fecha_actualizacion + '|') + str(v[i].likes) + '\n'
            m.write(dat)

    if not bandera:
        print('No se encontro ningun tag !!')

    m.flush()
    m.close()
    if bandera:
        print(f'\n --- Archivo "{fd}" creado...---')


def leer(arreglo):
    print(f'\nNombre de Usuario: {arreglo.nombre_usuario}', end=' | ')
    print(f'Repositorio: {arreglo.repositorio}', end=' | ')
    print(f'Descripcion: {arreglo.descripcion}', end=' | ')
    print(f'Fecha de Actualizacion: {arreglo.fecha_actualizacion}', end='| ')
    print(f'Lenguaje: {arreglo.lenguaje}', end=' | ')
    print(f'Likes: {arreglo.likes}', end=' | ')
    print(f'Tags: {arreglo.tags}', end=' | ')
    print(f'URL: {arreglo.url}')


def proyecto_actualizado(arreglo):
    if len(arreglo) == 0:
        print('\nNo hay datos cargados...')
        return

    search_rep = input('Ingrese un repositorio a buscar: ')
    tiene_rep = False
    n = len(arreglo)

    for i in range(n):
        if search_rep == arreglo[i].repositorio:
            search_url = input('Cargas una nueva URL: ')
            arreglo[i].url = search_url
            tiempo_news = datetime.datetime.now()
            tiempo = str(tiempo_news.year) + '-' + str( tiempo_news.month) + '-' + str(tiempo_news.day)
            arreglo[i].fecha_actualizacion = tiempo
            leer(arreglo[i])

            tiene_rep = True

    if not tiene_rep:
        print('\nNo se encontro el repositorio ' + search_rep)


def display_matriz(matriz):
    print('{:^10} | {:^10} | {:^10}'.format('Mes', 'Estrellas', 'Proyectos'))
    for i in range(len(matriz)):
        formato = '{:<10} | {:^10} | {:^10}'.format(matriz[i][0], matriz[i][1], matriz[i][2])
        print(formato)


def display_mes(matriz, mes):
    print('\n{:^10} | {:^10}'.format('Mes', 'Proyectos Totales'))
    formato = '{:<10} | {:^10}'.format(matriz[mes-1][0], matriz[mes-1][2])
    print(formato)


def popularidad(arreglo, ind):
    matriz = [] * 12
    acu_stars = [0] * 12
    acu_proyectos = [0] * 12

    if ind == 0:
        likes_por_estrellas(arreglo)

    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

    for i in range(len(arreglo)):
        acu_stars[(int(arreglo[i].fecha_actualizacion[5:7]))-1] += int(arreglo[i].likes)
        acu_proyectos[(int(arreglo[i].fecha_actualizacion[5:7]))-1] += 1

    for i in range(12):
        mini_matiz = [meses[i], acu_stars[i], acu_proyectos[i]]
        matriz.append(mini_matiz)

    display_matriz(matriz)

    print('\n---Total de Proyectos actualizados por Mes ---')
    mes = int(input('Ingrese un Mes (1 - 12): '))
    display_mes(matriz, mes)

    return matriz


def guardar_populares(matriz):
    m = open('matriz.csv', 'wb')

    for i in range(len(matriz)):
        if matriz[i][2] != 0:
            v = Matriz(matriz[i][0], matriz[i][1], matriz[i][2])
            pickle.dump(v, m)

    m.flush()
    m.close()


def display_bin(matriz):
    print('{:^20} | {:^20} | {:^20}'.format(matriz.mes, matriz.estrellas, matriz.cant_proyectos))


def mostrar_archivo():
    if not os.path.exists('matriz.csv'):
        print('Debe inicializar la opcion 6 primero...')
        return

    print(f'Contenido actual del archivo "matriz.csv"\n')
    m = open('matriz.csv', 'rb')
    t = os.path.getsize('matriz.csv')
    print('{:^20} | {:^20} | {:^20}'.format('Mes', 'Estrellas', 'Proyectos Totales'))
    while m.tell() < t:
        mat = pickle.load(m)
        display_bin(mat)
    m.flush()
    m.close()
