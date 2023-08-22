def add(*args):
    print(args[1])
    sum = 0;
    for n in args:
        sum += n
    return sum

print(add(1,2,3,4))

#basically dictionarty
def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        pass
    n += kwargs.get("add")
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)