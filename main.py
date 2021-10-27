# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import statistics
N1 = int(input("primer numero:"))
N2 = int(input("segundo numero:"))
N3 = int(input("tercer numero:"))

numeros = (N1,N2,N3)
media = statistics.mean(numeros)
mediana = statistics.median(numeros)
varianza = statistics.variance(numeros)



print("El resultado de la media ha sido media es:{media}")
print("El resultado de la mediana es:{mediana}")
print("el resultado de la varianza es:{varianza}")


