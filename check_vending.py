# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path


def run(operations_path: Path) -> bool:
    status_path = "data/vending/status.dat"
    updated_vending = {}
    cash_stock = {"1€": 0}

    error1 = "(E1: PRODUCT NOT FOUND)"
    error2 = "(E2: UNAVAILABLE STOCK)"
    error3 = "(E3: NOT ENOUGH USER MONEY)"

    # FUNCIÓN DE LECTURA
    def reading(reading_path: Path) -> list:
        with open(reading_path, "r") as f:
            for line in f:
                splitline = line.strip().split()
                # Los indices de splitline representarán un valor distinto dependiendo de la función
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
        return None

    # FUNCIÓN DE PEDIDO
    def order(code: str, qty: int, money: int) -> list:
        check = "❌"
        error = ""
        if code in updated_vending.keys():
            if qty <= updated_vending.get(code)[0]:
                if money >= updated_vending.get(code)[1] * qty:
                    updated_vending[code] = [
                        updated_vending.get(code)[0] - qty,
                        updated_vending.get(code)[1],
                    ]
                    cash_stock["1€"] += qty * updated_vending.get(code)[1]
                    check = "✅"
                else:
                    error = error3
            else:
                error = error2
        else:
            error = error1
        print(f"{check} 0 {code} {qty} {money} {error}")

    # FUNCIÓN DE REPOSICIÓN DE PRODUCTO
    def product_restock(code: str, qty: int) -> list:
        if code in updated_vending.keys():
            updated_vending[code] = [
                updated_vending.get(code)[0] + qty,
                updated_vending.get(code)[1],
            ]
        else:
            updated_vending[code] = [qty, 0]
        print(f"✅ R {code} {qty}")
        return None

    # FUNCIÓN DE CAMBIO DE PRECIO
    def price_update(code: str, price: int) -> list:
        if code in updated_vending.keys():
            updated_vending.get(code)[1] = price
            print(f"✅ P {code} {price}")
        else:
            print(f"❌ P {code} {price} {error1}")
        return None

    # FUNCIÓN DE REPOSICION DE DINERO
    def money_restock(cash: int) -> list:
        cash_stock["1€"] += cash
        print(f"✅ M {cash}")
        return None

    # FUNCIÓN DE ESCRITURA
    def writing(path: Path):
        with open(path, "w") as f:
            f.write(f"{cash_stock.get('1€')}\n")
            for item in sorted(updated_vending.keys()):
                f.write(
                    f"{item} {updated_vending.get(item)[0]} {updated_vending.get(item)[1]}\n"
                )
        return None

    # Se llama a la función de lectura
    reading("data/vending/operations.dat")

    return filecmp.cmp(status_path, "data/vending/.expected", shallow=False)


if __name__ == "__main__":
    run("data/vending/operations.dat")
