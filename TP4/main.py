from modulo import soporte

def main():
    fd = 'proyectos.csv'
    arreglo = []
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
            pass

        elif op == 3:
            leng = soporte.contar_lenguajes(fd)
            soporte.proyectos_por_lenguaje(arreglo, leng)

        elif op == 8:
            print('Saliendo...')


if __name__ == '__main__':
    main()
