'''Purpose'''

# This function will collect an user input to divide two numbers and return a percentage.
# This function will also error handle for the Value Error and the Zero Division Error. 


def fuel():
    try:
        fraction = input("Fraction: ")
        a, b = fraction.split("/")
        division = (int(a) / int(b)) * 100
    except (ValueError, ZeroDivisionError):
        print("You put in the wrong type of input or it was a zero") 
    else:
        print(f"{round(division)}%")
fuel()