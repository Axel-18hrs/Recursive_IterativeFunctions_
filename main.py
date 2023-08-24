# Function to calculate factorial iteratively
def iterative_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Function to calculate factorial recursively_
def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)

choice = int(input("// Choose an option:" +
      "\n[1]: iterative factorial" +
      "\n[2]: recursive factorial\n"))

if choice == 1:
    num = int(input("Enter a number: "))
    print(iterative_factorial(num))

if choice == 2:
    num = int(input("Enter a number: "))
    print(recursive_factorial(num))
