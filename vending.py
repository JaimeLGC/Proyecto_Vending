# ******************
# MÁQUINA DE VENDING
# ******************
import filecmp
from pathlib import Path


def run(operations_path: Path) -> bool:
    status_path = "data/vending/status.dat"
    # FUNCIÓN DE LECTURA
    # def lectura():
    # FUNCIÓN DE ESCRITURA

    # FUNCIÓN DE PEDIDO

    # FUNCIÓN DE REPOSICIÓN DE PRODUCTO

    # FUNCIÓN DE CAMBIO DE PRECIO

    # FUNCIÓN DE REPOSICION DE DINERO

    return filecmp.cmp(status_path, "data/vending/.expected", shallow=False)


if __name__ == "__main__":
    run("data/vending/operations.dat")
