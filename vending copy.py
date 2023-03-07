# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path


# CAMBIAR DATA !!!!!!!!!!!!!!!!!!!!!!


def run(operations_path: Path) -> bool:
    status_path = "vending/status.dat"
    # SE GUARDAN LOS DATOS ACTUALIZADOS PARA ORDENARLOS (Diccionario de listas)

    updated_vending = {}

    cash_stock = {"1€": 0}

    # FUNCIÓN DE LECTURA

    def reading(reading_path: Path) -> list:

        with open(reading_path, "r") as f:

            for line in f:

                splitline = line.strip().split()

                match splitline[0]:

                    case "O":

                        order(splitline[1], int(splitline[2]), int(splitline[3]))

                    case "R":

                        product_restock(splitline[1], int(splitline[2]))

                    case "P":

                        price_update(splitline[1], int(splitline[2]))

                    case "M":

                        money_restock(int(splitline[1]))

        writing(status_path)

    # FUNCIÓN DE PEDIDO

    def order(code: str, qty: int, money: int) -> list:

        if code in updated_vending.keys():

            if qty <= updated_vending.get(code)[0]:

                if money >= updated_vending.get(code)[1]:

                    product_restock(code, -qty)

                    money_restock(money - (qty * updated_vending.get(code)[1][1]))

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
            updated_vending.get(code, 0),
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
