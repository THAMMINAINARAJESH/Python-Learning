n = int(input("enter some value: "))
def FizzBuzz(n):
    for i in range(1 , n):
        if i % 3 == 0 and  i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif  i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    print("\n" * 2)
FizzBuzz(n)