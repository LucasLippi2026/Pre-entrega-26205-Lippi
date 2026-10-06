#Programa para registrar productos por su nombre, categoría y precio (Lucas Lippi)
Productos = []  #creo la lista en la que se guardan los productos

while True:  # Menú de opciones
    print("\033[47m\033[94m\033[1m-"*39)
    print("    Sistema de Gestión de Productos")
    print("-"*39)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar productos")
    print("4. Eliminar productos")
    print("5. Salir")
    opcion = input("Elegí una opción (1-5): ").strip()
    # Agregar productos en tres pasos para las tres cualidades (nombre, cat, $)
    if opcion == "1":
        print("\033[0m\033[47m\033[92m----- Agregar producto -----")
        while True:
            while True: # Validaciones del dato ingresado
                nombre = input("Nombre del producto (0 para salir): ").strip().title()
                if nombre == "0": # Opcion para volver al menú
                    break
                while nombre == "" or nombre.isdigit():
                    print("\033[91mError: el nombre ingresado no es valido\033[92m")
                    nombre = input("Nombre del producto (0 para salir): ").strip().title()
                break 
            if nombre == "0": # Opcion para volver al menú
                break
            while True:  # Validaciones del dato ingresado
                categoria = input("Categoría del producto: ").strip().title()
                while categoria == "" or categoria.isdigit():
                    print("\033[91mError: la categoría ingresada no es valido\033[92m")
                    categoria = input("Categoría del producto: ").strip().title() 
                break
            while True:  # Validaciones del dato ingresado
                precio_str = input("Ingrese el precio (sin centavos): ").strip()
                while not precio_str.isdigit():
                    print("\033[91mError: el precio ingresado no es valido\033[92m")
                    precio_str = input("Ingrese el precio (sin centavos): ").strip() 
                while precio_str == "0":
                    print("\033[91mError: el precio ingresado no es valido\033[92m")
                    precio_str = input("Ingrese el precio (sin centavos): ").strip()
                break
            precio = int(precio_str)  
            Productos.append([nombre,categoria,precio])    # Lo agrego a la lista
# Mostrar todos los productos de la lista con validacion por lista vacia
    elif opcion == "2":
        print("\033[96m----- Mostrar Productos -----")
        if len(Productos) == 0:
            print("\033[91mTodavía no hay productos cargados\033[96m")
        else:    
            for i in range(len(Productos)):
                print(f"Prod Nº: {i+1}  -Nombre: {Productos[i][0]:<15}  -Categoría: {Productos[i][1]:<12}   -Precio: ${Productos[i][2]:<10}")
# Buscar productos por nombre
    elif opcion == "3":
        print("\033[93m----- Buscar Productos -----")
        if len(Productos) == 0:  # Validacion lista vacia
            print("\033[91mTodavía no hay productos cargados")
        else:
            while True:
                busqueda = input("\033[93mNombre del producto a buscar (0 para salir): ").strip().title()
                if busqueda == "0":  # Opcion para volver al menú
                    break
                while busqueda == "":  # Validacion del dato ingresado
                    print("\033[91mERROR: No ingresó el nombre de un producto\033[93m")
                    busqueda = input("Nombre del producto a buscar (0 para salir): ").strip().title()
                    if busqueda == "0": # Opcion para volver al menú
                        break
                encontrado = 0
                for i in range(len(Productos)):  # Muesta el resultado de la búsqueda
                    if busqueda in Productos[i][0]:
                        print(f"Prod Nº: {i+1}  -Nombre: {Productos[i][0]:<15}  -Categoría: {Productos[i][1]:<12}   -Precio: ${Productos[i][2]:<10}")
                        encontrado += 1
                if encontrado == 0:
                    print("\033[91mNo se encontró ningún resultado.\033[93m")
                else:
                    print(f"\033[93mSe encontraron {encontrado} resultados.\033[93m")
# Opción eliminar productos de la lista
    elif opcion == "4":
        print("\033[95m----- Eliminar Productos -----")
        if len(Productos) == 0:  # Validacion lista vacia
            print("\033[91mNo hay productos para eliminar\033[95m")
        else:
            for i in range(len(Productos)):
                print(f"{i+1}.  {Productos[i][0]}    -{Productos[i][1]}    -{Productos[i][2]}") 
            while True:                   
                id_a_eliminar = input("Número de producto a eliminar (0 para salir): ").strip()
                if id_a_eliminar == "0": # Opcion para volver al menú
                    break
                while not id_a_eliminar.isdigit() or int(id_a_eliminar) > len(Productos):
                    print("\033[91mError: ingrese un número válido\033[95m")
                    id_a_eliminar = input("Número de producto a eliminar (0 para salir): ").strip()
                posicion = int(id_a_eliminar) - 1
                eliminado = Productos.pop(posicion)  
                print(f"Se eliminó el producto: \033[91m{eliminado[0]}\033[95m de la lista")  # Muestra el dato eliminado    
    elif opcion == "5":  # Finalizar el programa
        break            