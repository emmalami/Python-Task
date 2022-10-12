print("\na function that accepts two numbers")
def add(num1, num2):
    result= num1 + num2
    ("result:", result)
add(23,79)


print("\na function that return the string value")
def Academy(name):
    return name
module = Academy("Testify Python")
print(module)



def greet(name):
    print("Hello ", name)
greet("Olamide")


def argument(*args):
    print("arg ", args)
argument()
argument(1,2,3,4)

def check_number(number):
    if number > 5:
        return
    print("Number:", number)
print(check_number(4))