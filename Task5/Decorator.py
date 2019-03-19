def SavingFile(func):
    def wrapped(_dict, filename):
        with open(filename,"w", encoding="Utf-8") as file:
            file.write("Использовали декоратор!")
            return func(_dict, filename)
    return wrapped


