def getInput(calculate_fun):
    def wraps_function():
        s = print("This is a factorial program:")
        m = int(input("Enter number to calculate the factorial: "))
        calculate_fun(m)
    return wraps_function

@getInput
def factorial(num):
    fact = 1
    for i in range(num,0,-1):
        fact = i*fact
    print("factorial is : ", fact)

factorial()

