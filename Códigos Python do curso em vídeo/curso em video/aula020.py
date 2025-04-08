def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 0, 1, 2]
dobra(valores)
print(valores)

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(s)


soma(5, 2)
soma(2, 9, 4)
