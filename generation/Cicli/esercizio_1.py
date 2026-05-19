num = int(input("Inserire numero: "))
num_riserva = 0

while num != -1:
    num_riserva += num 
    num = int(input("Inserire numero: "))
print(num_riserva)