# use "*" to give as many positional arguments as you want, it is passed to the function as a tuple that you can iterate through, "args" is just the most used name
# use "**" to give keyword position arguments, it is passed as a dictionary with a key and value, "kwargs" is the most used name

# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum

# def calculate(n, **kwargs):
#     print(kwargs)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)


# sum = add(3, 4, 6, 7)
# print(sum)

# calculate(2, add=3, multiply=5)

# Use .get() function instead of [] so that you get None as the output when there are no value for a keyword argument
class Car:
    def __init__(self, **kw):
        self.model = kw.get("model")
        self.make = kw.get("make")

# my_car = Car(make = "Nissan", model = "GT-R")
my_car = Car(make = "Nissan")
print(my_car.make)
print(my_car.model)