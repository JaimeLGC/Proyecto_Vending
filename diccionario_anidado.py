demthings = "R D12 7"

updated_vending = {}
splitline = demthings.split()
if splitline[0] == "R":
    code = splitline[1]
    qty = int(splitline[2])


# updated_vending[code]["ammount"] = updated_vending.get(code["ammount"], 0) + qty
# updated_vending[code]["price"] = updated_vending.get(code["pric"], 0)
updated_vending[code] = [
    updated_vending.get(code, 0) + qty,
    updated_vending.get(code, 0),
]

if code in updated_vending.keys():
    print("lessgo")
else:
    print("yass")

print(updated_vending.get(code)[0])

print(updated_vending)
