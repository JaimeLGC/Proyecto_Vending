# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path


# CAMBIAR DATA !!!!!!!!!!!!!!!!!!!!!!


def run(operations_path: Path) -> bool:
    status_path = "vending/status.dat"

    # SE GUARDAN LOS DATOS ACTUALIZADOS PARA ORDENARLOS (Diccionario de listas)

    # Diccionario para los artículos, key: str / value: list
    updated_vending = {}

    # Diccionario único para el dinero, key: str / value: int
    cash_stock = {"1€": 0}

    # FUNCIÓN DE LECTURA

    def reading(reading_path: Path) -> list:

        # Lee el fichero de entrada
        with open(reading_path, "r") as f:

            # Recorre las lineas del fichero
            for line in f:

                # Splitline: List // Separa las lineas por espacios
                splitline = line.strip().split()

                # Match Case, llama a una función dependiendo del codigo que se encuentra en el primer item de Splitline
                match splitline[0]:

                    case "O":

                        # Splitline 1 -> Codigo / Splitline 2 -> Cantidad / Splitline 3 -> Dinero
                        order(splitline[1], int(splitline[2]), int(splitline[3]))

                    case "R":

                        # Splitline 1 -> Codigo / Splitline 2 -> Cantidad
                        product_restock(splitline[1], int(splitline[2]))

                    case "P":

                        # Splitline 1 -> Codigo / Splitline 2 -> Precio
                        price_update(splitline[1], int(splitline[2]))

                    case "M":

                        # Splitline 1 -> Dinero
                        money_restock(int(splitline[1]))

        writing(status_path)

    # FUNCIÓN DE PEDIDO

    def order(code: str, qty: int, money: int) -> list:

        # Comprueba que el producto existe buscando su codigo en las llaves del diccionario
        if code in updated_vending.keys():

            # Comprueba que hay stock comparando la cantidad pedida con el primer elemento de la lista del valor del articulo en el diccionario
            if qty <= updated_vending.get(code)[0]:

                # Comprueba que el dinero introducido es mayor que el precio (segundo elemento de la lista del valor del artículo)
                if money >= updated_vending.get(code)[1]:

                    # Elimina los productos comprados del stock haciendo la funcion de restock con un valor negativo
                    product_restock(code, -qty)

                    # OJO CON ESTE
                    # Añade a las monedas el precio del producto multiplicada por la cantidad para saltarse el cambio
                    money_restock(qty * updated_vending.get(code)[1])

                # ERRORES

                else:

                    return "Error 1"

            else:

                return "Error 2"

        else:

            return "Error 3"

    # FUNCIÓN DE REPOSICIÓN DE PRODUCTO

    def product_restock(code: str, qty: int) -> list:

        updated_vending[code] = [
            updated_vending.get(code[0], 0) + qty,
            updated_vending.get(code[1], 0),
        ]

        return "product_restock"

    # FUNCIÓN DE CAMBIO DE PRECIO

    def price_update(code: str, price: int) -> list:

        if code in updated_vending.keys():

            updated_vending.get(code)[1] = price

        return "price_update"

    # FUNCIÓN DE REPOSICION DE DINERO

    def money_restock(cash: int) -> list:

        cash_stock["1€"] += cash

        return "money_restock"

    # FUNCIÓN DE ESCRITURA

    def writing(path: Path):

        with open(path, "w") as f:

            f.write(f"{cash_stock.get('1€')} \n")

            for item in updated_vending.keys():

                f.write(
                    f"{item} {updated_vending.get(item)[0]} {updated_vending.get(item)[1]} \n"
                )

    reading("vending/operations.dat")

    return filecmp.cmp(status_path, "vending/.expected", shallow=False)


if __name__ == "__main__":
    run("vending/operations.dat")
