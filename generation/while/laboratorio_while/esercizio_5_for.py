for i in range(5):
    num = int(input("Inserire numero: "))
    if i == 0:
        num_min = num

    if num < num_min:
        num_min = num
print(num_min)