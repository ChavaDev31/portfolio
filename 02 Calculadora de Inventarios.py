#Diccionario con el inventario inicial vacío
inventario= {}

#Mensaje de bienvenida
print("Bienvenido a la calculadora de inventario")

#Bucle principal
while True:
    #Menú de opciones
    print("\nPor favor elige una opción")
    print("1. Agregar un producto")
    print("2. Eliminar un producto")
    print("3. Actualizar la cantidad de un producto")
    print("4. Mostrar todo el inventario")
    print("5. Salir")

    opcion = input("Ingresa el número de la opción deseada: ")

    if opcion =="1":
        nombre_producto = input("Por favor escribe el nombre del producto ")
        try:
            cantidad = int(input(f"Ingresa la cantidad para '{nombre_producto}': "))
            if cantidad <0:
               print("Por favor, ingresa un número positivo para la cantidad.")
            else:
                if nombre_producto in inventario:
                    print(f"El producto '{nombre_producto}' ya existe. Actualizando la cantidad...")
                    inventario[nombre_producto] += cantidad  
                else: 
                    inventario[nombre_producto] = cantidad
                print(f"Producto '{nombre_producto}' agregado exitosamente con {cantidad} unidad(es).")
        except ValueError:
            print("Por favor, ingresa un número válido para la cantidad")

    elif opcion == "2":
        nombre_producto =input("Por favor escriba el nombre del producto a eliminar ")
        if nombre_producto in inventario:
            del inventario [nombre_producto]
            print(f"Producto '{nombre_producto}' eliminado del inventario.")
        else:
                print(f" El producto {nombre_producto} no existe en el inventario")
                      
    elif opcion == "3":
        nombre_producto = input("Por favor escribe el nombre del producto al cual se actualizará su cantidad. ")
        if nombre_producto in inventario:
            try:
                nueva_cantidad = int(input(f"Ingresa la nueva cantidad para '{nombre_producto}': "))
                if nueva_cantidad <0:
                    print("Por favor, ingresa un número positivo para la cantidad. ")
                else:
                    inventario[nombre_producto] = nueva_cantidad
                    print(f"El producto '{nombre_producto}' se actualizó exitosamente a {nueva_cantidad} unidad(es).")
            except ValueError:
             print("Por favor, ingresa un número válido para la cantidad.")
        else :
            print(f"El producto '{nombre_producto}' no existe en el inventario. Intenta guardarlo primero.")
    
    elif opcion == "4":
        if inventario:
            print("\nInventario actual: ")
            for producto, cantidad in inventario.items():
                print(f"- {producto}: {cantidad} unidad(es)")
        else:
            print("El inventario está vacío.")
            
    elif opcion =="5":
        print("Gracias por usar la Calculadora de Inventario.")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")