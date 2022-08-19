def move(fro, to):
    print(f"Move {fro} to {to}")

#first arg is from, the second arg is the aux the third arg is the target
def hanoi(n,first, second, third):
    if n == 0:
        pass
    else:
        hanoi(n-1, first, third, second)
        move(first, third)
        hanoi(n-1, second, first, third)


hanoi(5, "A", "B", "C")


