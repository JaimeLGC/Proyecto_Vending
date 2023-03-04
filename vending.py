# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path


def run(operations_path: Path) -> bool:
    status_path = "data/vending/status.dat"
    # FUNCIÓN DE LECTURA
    def reading(operations_path: Path) -> list:
        with open(operations_path, "r") as f:
            for line in f:
                splitline = line.strip().split()
                match splitline[1]:
                    case "O":
                        print("order")
                    case "R":
                        print("función2")
                    case "P":
                        print("función3")
                    case "M":
                        print("función4")

    # FUNCIÓN DE ESCRITURA

    # FUNCIÓN DE PEDIDO
    def order(code: str, qty: int, money: int):
        return "order"

    # FUNCIÓN DE REPOSICIÓN DE PRODUCTO
    def product_restock(code: str, qty: int):
        return "product_restock"

    # FUNCIÓN DE CAMBIO DE PRECIO
    def price_update(code: str, price: int):
        return "price_update"

    # FUNCIÓN DE REPOSICION DE DINERO
    def money_restock(qty: int):
        return "money_restock"

    return filecmp.cmp(status_path, "data/vending/.expected", shallow=False)


if __name__ == "__main__":
    run("data/vending/operations.dat")
