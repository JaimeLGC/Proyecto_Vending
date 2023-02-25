# MÁQUINA DE VENDING

# VERSIÓN PRUEBAS 1.0

# Recibe la orden como un diccionario 'Valor:Cantidad'
order = {"coke": 2, "cookies": 3}

# Diccionario anidado con precio y stock
prices_and_stock = {
    "water": {"price": 0.5, "stock": 15},
    "cookies": {"price": 1, "stock": 26},
    "coke": {"price": 2, "stock": 37},
    "snacks": {"price": 1.50, "stock": 20},
    "fries": {"price": 1, "stock": 15}
}

# Creamos una varibable para lo que debemos pagar
must_pay = 0

# (Prueba sujeta a cambios) mostrar al cliente visual de la maquina con producto y código

machine = [["water", "0.5"],["cookies","1"],["coke","2"],["snacks","1.50"],["fries", "1"]]
for product in machine:
    print(product)
# Función para la acción de realizar un pedido
def _request(product, stock):
    for product in order.keys():
        # Revisión si el producto esta en stock o no
        if product not in prices_and_stock:
            print("Actualmente no tenemos ese producto en stock")
        # Revisión de si la maquina tiene la suficiente cantidad de lo que nos pide
        elif prices_and_stock.get(product).get("stock") < order.get(product):
            print(f"Actualmente no contamos con esa cantidad en stock")
        # Si tanto el stock y la cantidad estan bien calculamos lo que debemos pagar
        else:
            must_pay += prices_and_stock.get(product).get("price") * order.get(product)

        
