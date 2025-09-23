# Program to check if a number is even or odd, and find its square and cube using functions.
def even_odd(num):
    """Check if a number is even or odd."""
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

def square(num):
    """Return the square of a number."""
    return num ** 2

def cube(num):
    """Return the cube of a number."""
    return num ** 3

def main():
    """Main function to run the program."""
    num = int(input("Enter a number: "))
    print("The number is:", even_odd(num))
    print("Square:", square(num))
    print("Cube:", cube(num))
main()