# square of N number
def square_gener():

    N = int(input("Enter a number: "))


    for i in range(1, N + 1):
        yield i ** 2

for square in square_gener():
    print(square)







# even numbers.
def even_generator(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number: "))

even_nums = even_generator(n)

print(",".join(str(num) for num in even_nums))





# Divisable by 3 and 4.
def divisible_generator(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number: "))

divisible_nums = divisible_generator(n)

for num in divisible_nums:
    print(num)
    print()
    print()







# Square of all numbers between a and b
def squares(a, b):
    for i in range(a, b+1):
        yield i ** 2

for num in squares(1, 5):
    print(num)





# Numbers from n down to 0.
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
# Test the countdown generator
for i in countdown(5):
    print()
    print(i)
