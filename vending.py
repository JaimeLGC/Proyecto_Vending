# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path

status_path = "data/vending/status.dat"

# VARIABLES DE GUARDADO
updated_vending = {}
cash_stock = {"1€": 0}

# FUNCIÓN DE LECTURA
def reading(reading_path: Path) -> None:
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
def order(code: str, qty: int, money: int) -> None:
    if code in updated_vending.keys():
        if qty <= updated_vending.get(code)[0]:
            if money >= updated_vending.get(code)[1] * qty:
                product_restock(code, -qty)
                money_restock(qty * updated_vending.get(code)[1])


# FUNCIÓN DE REPOSICIÓN DE PRODUCTO
def product_restock(code: str, qty: int) -> None:
    if code in updated_vending.keys():
        updated_vending[code] = [
            updated_vending.get(code)[0] + qty,
            updated_vending.get(code)[1],
        ]
    else:
        updated_vending[code] = [qty, 0]


# FUNCIÓN DE CAMBIO DE PRECIO
def price_update(code: str, price: int) -> None:
    if code in updated_vending.keys():
        updated_vending.get(code)[1] = price


# FUNCIÓN DE REPOSICION DE DINERO
def money_restock(cash: int) -> None:
    cash_stock["1€"] += cash


# FUNCIÓN DE ESCRITURA
def writing(path: Path) -> None:
    with open(path, "w") as f:
        f.write(f"{cash_stock.get('1€')}\n")
        for item in sorted(updated_vending.keys()):
            f.write(
                f"{item} {updated_vending.get(item)[0]} {updated_vending.get(item)[1]}\n"
            )


def run(operations_path: Path) -> bool:
    reading("data/vending/operations.dat")
    return filecmp.cmp(status_path, "data/vending/.expected", shallow=False)


if __name__ == "__main__":
    run("data/vending/operations.dat")
