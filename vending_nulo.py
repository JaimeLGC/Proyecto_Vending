# MÁQUINA DE VENDING

# VERSIÓN NULA

# Recibe la orden como un diccionario 'Valor:Cantidad'
order = {"coke": 2, "cookies": 3}

# Diccionario anidado con precio y stock
prices_and_stock = {
    "water": {"price": 0.5, "stock": 15},
    "cookies": {"price": 1, "stock": 26},
    "coke": {"price": 2, "stock": 37},
}
# Recibo, suma los precios a pagar
receipt = 0

# Deshecha los productos no existentes y los fuera de stock
# Suma los pedidos válidos al recibo y lo imprime
for item in order.keys():
    if item not in prices_and_stock.keys():
        print("no válido")
    elif prices_and_stock.get(item).get("stock") < order.get(item):
        print("no válido")
    else:
        receipt += prices_and_stock.get(item).get("price") * order.get(item)
print(receipt)