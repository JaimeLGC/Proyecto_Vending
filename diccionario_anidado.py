demthings = "R D12 7"

updated_vending = {}
splitline = demthings.split()
match splitline[1]:
    case "R":
        code = splitline[2]
        qty = splitline[3]


updated_vending[code]["ammount"] = updated_vending.get(code["ammount"], 0) + qty
updated_vending[code]["price"] = updated_vending.get(code["pric"], 0)

print(updated_vending)
