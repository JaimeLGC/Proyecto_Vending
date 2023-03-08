# placeholder
demthings = "R D12 7 / P D12 2"

updated_vending = {}

things = demthings.split("/")
for thing in things:
    splitline = thing.split()
    if splitline[0] == "R":
        code = splitline[1]
        qty = int(splitline[2])
    elif splitline[0] == "P":
        code = splitline[1]
        qty = -int(splitline[2])

    if code in updated_vending.keys():
        updated_vending[code] = [
            updated_vending.get(code)[0] + qty,
            updated_vending.get(code)[1],
        ]
    else:
        updated_vending[code] = [qty, 0]

    if code in updated_vending.keys():
        print("lessgo")
    else:
        print("yass")

    print(updated_vending.get(code, 0)[0])

    print(updated_vending)
