# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path


def run(operations_path: Path) -> bool:
    status_path = "data/vending/status.dat"
    # SE GUARDN LOS DATOS ACTUALIZADOS PARA ORDENARLOS (Lista de listas)
    updated_vending = {}
    vending_items = []
    cash_stock = 0
    # FUNCIÓN DE LECTURA
    def reading(operations_path: Path) -> list:
        with open(operations_path, "r") as f:
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
        if code in vending_items:
            if qty <= vending_items.get(code)[0]:
                if money >= vending_items.get(code)[1]:
                    return "order"

    # FUNCIÓN DE REPOSICIÓN DE PRODUCTO
    def product_restock(code: str, qty: int) -> list:
        vending_items.append(code)
        updated_vending[code] = [
            updated_vending.get(code, 0) + qty,
            updated_vending.get(code, 0),
        ]
        return "product_restock"

    # FUNCIÓN DE CAMBIO DE PRECIO
    def price_update(code: str, price: int) -> list:
        if code in vending_items:
            updated_vending.get(code)[1] = price
        return "price_update"

    # FUNCIÓN DE REPOSICION DE DINERO
    def money_restock(cash: int) -> list:
        cash_stock += cash
        return "money_restock"

    # FUNCIÓN DE ESCRITURA
    # placeholder
    return filecmp.cmp(status_path, "data/vending/.expected", shallow=False)


if __name__ == "__main__":
    run("data/vending/operations.dat")
