stevilo1 = int(input("Vnesite 1. celo število:"))
stevilo2 = int(input("Vnesite 2. celo število:"))

if stevilo1 > stevilo2:
    stevilo1 = stevilo1 / 3
    stevilo2 = stevilo2 / 2

    if stevilo1 > stevilo2:
        print("Tvoje prvo število je po delitvi postalo največje in znaša " + str(stevilo1))
    else:
        print("Tvoje drugo število je po delitvi postalo največje in znaša " + str(stevilo2))
else:
    stevilo2 = stevilo2 / 3
    stevilo1 = stevilo1 / 2

    if stevilo1 > stevilo2:
        print("Tvoje prvo število je po delitvi postalo največje in znaša " + str(stevilo1))
    else:
        print("Tvoje drugo število je po delitvi postalo največje in znaša " + str(stevilo2))