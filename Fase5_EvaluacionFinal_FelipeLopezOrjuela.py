#inventario
inventario = [
    [101, "Procesador Intel Core I7", 20, 35],
    [102,"Memoria RAM DDR5 16GB", 30, 28],
    [103,"Disco SSD 1TB", 15, 32],
    [104,"Tarjeta Grafica RTX 4060", 12, 40],
    [105,"Fuente de Poder 650W", 25, 30],
    [106,"Placa Base ATX", 18, 43]
]

#Calculo de la matriz
def calcular_reabastecimiento(articulo):
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        cantidad = 0
    return cantidad

#consulta estado
def consultar_estado(articulo):
    print("\n===== Estado del articulo=====")
    print("codigo:", articulo[0])
    print("Nombre:", articulo[1])
    print("Stock Actual:", articulo[2])
    print("Stock Minimo", articulo[3])

    cantidad = calcular_reabastecimiento(articulo)
    if cantidad > 0:
        print("Estado: Necesita reabastecimiento")
    else:
        print("Estado: Stock suficiente")
    print("Cantidad necesaria:", cantidad)

#actualizar stock
def actualizar_stock(articulo):
    print("Articulo:", articulo[1])
    print("Stock anterior:", articulo[2])

    try:
        nuevo_stock = int(input("Ingrese el nuevo stock total: "))
        if nuevo_stock < 0:
            print("Error: El stock no puede ser negativo.")
            return
        stock_anterior = articulo[2]
        articulo[2] = nuevo_stock
        print("\n=====Acutualizacion exitosa=====")
        print("Stock anterior:", stock_anterior)
        print("Stock actualizado:", articulo[2])
        print("Diferencia:", articulo[2] - stock_anterior)
        cantidad = calcular_reabastecimiento(articulo)
        if cantidad > 0:
            print("Faltan", cantidad, "Unidades para alcanzar el minimo.")
        else:
            print("El articulo tiene stock suficiente.")
    except ValueError:
        print("Error: Debe ingresar un numer entero.")

#reporte general
def reporte_general():
    print("\n=====Reporte General=====")
    total_articulos = len(inventario)
    total_stock = 0
    articulos_reabastecer = 0
    total_solicitar = 0

    for articulo in inventario:
        codigo = articulo[0]
        nombre = articulo[1]
        stock = articulo[2]
        minimo = articulo[3]
        cantidad = calcular_reabastecimiento(articulo)
        total_stock += stock
        if cantidad > 0:
            articulos_reabastecer += 1
            total_solicitar += cantidad
            estado = "Reabastecer"
        else:
            estado = "Suficiente"
        print("\nCodigo:", codigo)
        print("Articulo:", nombre)
        print("Stock actual:", stock)
        print("Stock minimo:", minimo)
        print("Estado:", estado)
        print("Cantida a solicitar:", cantidad)

    print("\n=====Resumen=====")
    print("Total de articulos:", total_articulos)
    print("Total de unidades en inventario", total_stock)
    print("Articulos por reabastecer:", articulos_reabastecer)
    print("Total de unidades a solicitar", total_solicitar)

#lista de articulos
def listar_articulos():
    print("\n=====Inevtario disponible======")
    for articulo in inventario:
        print(articulo[0],"-", articulo[1])

#menu por articulo
def menu_articulo(articulo):
    while True:
        print("\n=====Menu del Articulo=====")
        print("Articulo:", articulo[1])
        print("1. Consultar estado del articulo")
        print("2. Actualizar stock")
        print("3. Consultar cantidad de reabastecimiento")
        print("4. Volver al menu principal")

        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            consultar_estado(articulo)
        elif opcion == "2":
            actualizar_stock(articulo)
        elif opcion == "3":
            cantidad = calcular_reabastecimiento(articulo)
            print("\nCantidad necesaria para solicitar:", cantidad)
        elif opcion == "4":
            break
        else:
            print("Opcion no valida. Intente nuevamente.")

#seleccionar 
def seleccionar_articulo():
    listar_articulos()
    try:
        codigo = int(input("\nIngrese el codigo del articulo: "))
        for articulo in inventario:
            if articulo[0] == codigo:
                menu_articulo(articulo)
                return
        print("No se encontro un articulo con este codigo.")
    except ValueError:
        print("Error: Ingrese un codigo numerico valido.")

#menu principal
def menu_principal():
    while True:
        print("\n=====Sistema de inventario 2.0=====")
        print("1. Seleccionar articulo")
        print("2. Reporte general del inventario")
        print("3. Consultar articulos por reabastecer")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            seleccionar_articulo()
        elif opcion == "2":
            reporte_general()
        elif opcion == "3":
            print("\n=====Articulos por reabastecer=====")
            for articulo in inventario:
                cantidad = calcular_reabastecimiento(articulo)
                if cantidad > 0:
                    print(articulo[1], "-", cantidad, "unidades")
        elif opcion == "4":
            print("\nGracias por usar el sistema.")
        else:
            print("Opcion no valida. Intente nuevamente.")

#ejecucion
menu_principal()