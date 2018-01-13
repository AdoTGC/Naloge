zacetno_stanje = 1000

numbers = []
for i in range(1,11):
    numbers.append(int(input("Vnesite " + str(i) + ". število:")))

for i in numbers:
    i = i * 0.5
    zacetno_stanje = zacetno_stanje - i

print("Od začetnega stanja je ostala vrednost " + str(zacetno_stanje))