import itertools

amount = input("Enter the amount of children:")
if not all(ch in "0123456789" for ch in amount):
    print("Invalid input for the amount of children - Enter a positive Integer")
else:
    amount = int(amount)
    power = pow(2, amount)
    boy = "Boy"
    girl = "Girl"
    sample_space = list(itertools.product([boy, girl], repeat=amount))
    print(sample_space)

    ans = 0
    for i in sample_space:
        k=0
        for j in i:
            if 'Girl' in j:
                k=k+1
        if k == 2:
            ans = ans+1
    print(ans/power)