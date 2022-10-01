from modulo import soporte


def main():
    fd = 'proyectos.csv'
    arreglo = []
    matriz_total = []
    ind = 0
    menu ='\nEscoja una opcion\n' \
          '1. Cargar\n' \
          '2. Flitrar por tags\n' \
          '3. Lenguajes\n' \
          '4. Popularidad\n' \
          '5. Busacar protectos actualizado\n' \
          '6. Guardar populares\n' \
          '7. Mostrar archivo\n' \
          '8. Salir\n'

    op = 0
    while op != 8:
        fd = 'proyectos.csv'

        print(menu)
        op = int(input('Seleccione una Opcion: '))

        if op == 1:

            repositorios_sin_repetir = soporte.repos()
            arreglo = soporte.cargar_archivo(fd, repositorios_sin_repetir)

        elif op == 2:
            soporte.filtrar_tag(arreglo)

        elif op == 3:
            if len(arreglo) != 0:
                leng = soporte.contar_lenguajes(fd)
                soporte.proyectos_por_lenguaje(arreglo, leng)
            else:
                print('Opcion "1. Cargar" para continuar')

        elif op == 4:
            if len(arreglo) != 0:
                matriz_total = soporte.popularidad(arreglo, ind)
                ind += 1
            else:
                print('\nCargar Arreglo...')
                print('Opcion "1. Cargar" para continuar')

        elif op == 5:
            soporte.proyecto_actualizado(arreglo)

        elif op == 6:
            if len(matriz_total) != 0:
                soporte.guardar_populares(matriz_total)
            else:
                print('\nCargue la Matriz...')
                print('Opcion "4. Popularidad" para continuar')

        elif op == 7:
            soporte.mostrar_archivo()

        elif op == 8:
            print('Saliendo...')


if __name__ == '__main__':
    main()
