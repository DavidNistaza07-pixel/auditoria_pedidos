# Registro de pedidos - codigo original para auditoria
# Version sin validaciones (traduccion del pseudocodigo de la consigna)

print("=== REGISTRO DE PEDIDOS ===")

# Entrada de datos con mensajes directos
producto = input("Nombre del producto: ")
cantidad = int(input("Cantidad solicitada: "))
precio = float(input("Precio unitario: "))
descuento = float(input("Porcentaje de descuento: "))

# Cálculo del total
total = cantidad * precio
total = total - (total * descuento / 100)

# Resumen del pedido
print("\n--- RESUMEN DE LA COMPRA ---")
print("Producto:", producto)
print("Cantidad:", cantidad)
print("Total a pagar: $", round(total, 2))

# Confirmación del pedido
print("\n¿Desea confirmar el pedido?")
print("1. Sí")
print("2. No")
opcion = int(input("Seleccione una opción (1 u 2): "))

# Estructura condicional bien indentada
if opcion == 1:
    print("\n¡Pedido confirmado con éxito!")
else:
    print("\nPedido cancelado.")

print("Proceso finalizado.")