# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path


def run(operations_path: Path) -> bool:
    status_path = "data/vending/status.dat"
    # SE GUARDN LOS DATOS ACTUALIZADOS PARA ORDENARLOS (Lista de listas)
    updated_vending = {}
    # FUNCIÓN DE LECTURA
    def reading(operations_path: Path) -> list:
        with open(operations_path, "r") as f:
            operations = f.readlines()
            for line in f:
                splitline = line.strip().split()
                match splitline[0]:
                    case "O":
                        order(splitline[1], splitline[2], splitline[3])
                    case "R":
                        product_restock(splitline[1], splitline[2])
                    case "P":
                        price_update(splitline[1], splitline[2])
                    case "M":
                        money_restock(splitline[1])

    # FUNCIÓN DE PEDIDO
    def order(code: str, qty: int, money: int) -> list:
        return "order"

    # FUNCIÓN DE REPOSICIÓN DE PRODUCTO
    def product_restock(code: str, qty: int) -> list:
        updated_vending[code]["ammount"] = (
            updated_vending.get(code).get("ammount", 0) + qty
        )
        updated_vending[code]["price"] = updated_vending.get(code["pric"], 0)
        return "product_restock"

    # FUNCIÓN DE CAMBIO DE PRECIO
    def price_update(code: str, price: int) -> list:

        return "price_update"

    # FUNCIÓN DE REPOSICION DE DINERO
    def money_restock(qty: int) -> list:
        return "money_restock"

    # FUNCIÓN DE ESCRITURA
    # placeholder
    return filecmp.cmp(status_path, "data/vending/.expected", shallow=False)


if __name__ == "__main__":
    run("data/vending/operations.dat")
