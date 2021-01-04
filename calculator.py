import re

previous = 0
run = True

print("My Magical Calculator")
print("Type 'quit' to exit\n")


def preform_math():
    global run
    global previous

    equation = input("equation: ")
    equation = re.sub('[a-zA-Z:.,()" "]', '', equation)

    if equation == 'quit':
        print("Good Bye!")
        run = False
    else:
        previous = eval(equation)
        print("result is: ", previous)


while run:
    preform_math()
