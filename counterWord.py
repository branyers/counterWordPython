from collections import Counter


def frecuencywordonfile(namefile):
    try:
        file = open(f"{namefile}.txt")
        for word in file:
            palabras = word.split()
            return Counter(palabras).most_common(10)

    except FileNotFoundError:
        print("El archivo no fue encontrado")


print(frecuencywordonfile("holaMundo"))


