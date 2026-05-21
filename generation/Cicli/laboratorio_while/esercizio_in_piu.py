carta = 0.08
luna = 384400
luna_mm = luna * 1000000
sole = 149600000
sole_mm = sole * 1000000

cont_luna = 0
cont_sole = 0
while True:
    cont_luna += 1
    carta *= 2
    if carta > luna_mm:
        break
print(cont_luna)

carta = 0.08
while True:
    cont_sole += 1
    carta *= 2
    if carta > sole_mm:
        break
print(cont_sole)